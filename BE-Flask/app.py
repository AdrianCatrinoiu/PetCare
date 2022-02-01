from ast import While
from flask import Flask
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap
import os
from objects import PetCareObject
from threading import Thread
import time
import json

import db
import environment
import status_api
import status
import food
import water

petCareObject = PetCareObject()


thread = None


def create_mqtt_app():

    # Setup connection to mqtt broker
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['MQTT_BROKER_URL'] = 'localhost'
    app.config['MQTT_BROKER_PORT'] = 1883
    app.config['MQTT_USERNAME'] = ''
    app.config['MQTT_PASSWORD'] = ''
    app.config['MQTT_KEEPALIVE'] = 5
    app.config['MQTT_TLS_ENABLED'] = False
    app.config['MQTT_CLEAN_SESSION'] = True

    global mqtt
    mqtt = Mqtt(app)
    global socketio
    socketio = SocketIO(app, async_mode="eventlet")

    return mqtt


# Function that every second publishes a message
def background_thread():
    count = 0
    while True:
        time.sleep(1)
        # Using app context is required because the get_status() functions
        # requires access to the db.
        with app.app_context():
            message = json.dumps(status.get_status(), default=str)
        # Publish
        mqtt.publish('python/mqtt', message)


def create_app():
    global app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    @app.route('/')
    def hello_world():
        # Here I chose to start the periodic publishing after the root endpoint is called.
        # It's not the best nor cleaneste approach, but will have to refactor it.
        # What is important is that the background_thread function is called on
        # a separate thread, so that publishing can happen while simultaneously
        # HTTP endpoints are also functional.

        global thread
        if thread is None:
            thread = Thread(target=background_thread)
            thread.daemon = True
            thread.start()
        return 'Hello World!'

    db.init_app(app)
    app.register_blueprint(environment.bp)
    app.register_blueprint(food.bp)
    app.register_blueprint(status_api.bp)
    app.register_blueprint(water.bp)
    socketio = SocketIO(app)
    bootstrap = Bootstrap(app)


    """
	    Rutele pentru butonul de apa
    """

    @app.route('/start-water-sensor')
    def startWaterSensor():
        petCareObject.startWaterSensor()
        mqtt.publish('water/level', str(petCareObject.getWaterLevel()))
        return 'Water sensor is opened'

    @app.route('/stop-water-sensor')
    def stopWaterSensor():
        petCareObject.stopWaterSensor()
        mqtt.publish('water/level', str(petCareObject.getWaterLevel()))
        return 'Water sensor is closed'

    @app.route('/get-water-level')
    def getWaterLevel():
        mqtt.publish('water/level', str(petCareObject.getWaterLevel()))
        return f'Your water level is {petCareObject.getWaterLevel()}.'

    @app.route('/make-water-empty')
    def makeWaterEmpty():
        petCareObject.makeWaterEmpty()
        return 'make water empty'

    """
        Buton pentru hranire
    """

    @app.route('/start-food-sensor')
    def startFoodSensor():
        petCareObject.startFoodSensor()
        mqtt.publish('food/level', str(petCareObject.getFoodLevel()))
        return 'Food sensor is opened'

    @app.route('/stop-food-sensor')
    def stopFoodSensor():
        petCareObject.stopFoodSensor()
        mqtt.publish('food/level', str(petCareObject.getFoodLevel()))
        return 'Food sensor is closed'

    @app.route('/get-food-level')
    def getFoodLevel():
        mqtt.publish('food/level', str(petCareObject.getFoodLevel()))
        return f'Your food level is {petCareObject.getFoodLevel()}.'

    @app.route('/make-food-empty')
    def makeFoodEmpty():
        petCareObject.makeFoodEmpty()
        mqtt.publish('food/level', str(petCareObject.getFoodLevel()))
        return 'make food empty'

    return app



def mqttClient():
    mqttClient = mqtt.Client()
    mqttClient.username_pw_set('', '')
    topics = ['food/level', 'water/level', 'thermometer/level']

    def on_message(client, userdata, msg):
        print('###################')
        print(msg)

    for topic in topics:
        mqttClient.subscribe(topic)
        mqtt.on_message = on_message

    mqttClient.connect('localhost')
    mqttClient.loop_start()


def run_socketio_app():
    create_app()
    socketio = SocketIO(app)
    bootstrap = Bootstrap(app)
    create_mqtt_app()
    socketio.run(app, host='localhost', port=5000,
                 use_reloader=False, debug=True)


if __name__ == '__main__':
    os.environ['FLASK_ENV'] = 'development'
    socketio.run(app, host='0.0.0.0', port=5000, use_reloader=True, debug=True)
    mqttClient()
    run_socketio_app()
