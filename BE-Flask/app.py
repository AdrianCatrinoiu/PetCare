from flask import Flask
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap
from flask_swagger_ui import get_swaggerui_blueprint
import os
from threading import Thread
import time
import json
from paho.mqtt import client as mqtt_client

import db
import environment
import status_api
import status
import food
import water
import sound


thread = None
socketio = None


### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "PetCare"
    }
)
app = None
client = None
broker = 'broker.emqx.io'
port = 1883
topic = 'petCare'
client_id = f'python-mqtt-1'
username = ''
password = ''


def get_mqtt_client():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish_message(client, message):
    result = client.publish(topic, message)
    status = result[0]

    if status == 0:
        print(f'Sent message `{message}`')
        return 'ok'
    else:
        print(f'Failed to send message to topic {topic}')
        return 'fail'


def create_app():
    global app, socketio
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    client = get_mqtt_client()

    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
    # ### end swagger specific ###
    app.register_blueprint(water.get_blueprint())

    @app.route('/')
    def hello_world():
        publish_message(client, 'Hello world from mqtt')
        return 'Hello World!'

    db.init_app(app)
    app.register_blueprint(environment.bp)
    app.register_blueprint(food.bp)
    app.register_blueprint(status_api.bp)
    app.register_blueprint(water.bp)
    app.register_blueprint(sound.bp)
    socketio = SocketIO(app)
    bootstrap = Bootstrap(app)
    return app


def run_socketio_app():
    create_app()
    socketio = SocketIO(app)
    socketio.run(app, host='0.0.0.0', port=5000,
                 use_reloader=True, debug=True)


if __name__ == '__main__':
    os.environ['FLASK_ENV'] = 'development'
    run_socketio_app()
