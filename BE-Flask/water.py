from flask import (
    Blueprint, request, jsonify
)
import os
import sys
from db_v2 import DB
import app
import json
bp = Blueprint('water', __name__, url_prefix='/water')

sys.path.append(os.path.join(os.path.dirname(__file__), 'ButtonForFeeding'))
import ButtonForFeedingModel

db2 = DB()

f = open('paramConfig.json')
parameterConfig = json.load(f)
parameterConfig = parameterConfig['feeding']['water']

waterButton = ButtonForFeedingModel.ButtonForFeeding('Water',parameterConfig['feedingPush'],parameterConfig['feedingTimer'],parameterConfig['bellTimer'])


def get_blueprint():
    """Return the blueprint for the main app module"""
    return bp


@bp.route('/', methods=('GET', 'POST'))
def get_water():
    client = app.get_mqtt_client()
    app.publish_message(client, 'Get water history')
    return jsonify({
        'table': 'Water',
        'rows': db2.getTableData('water')}), 200


@bp.route('/start-water-sensor', methods=('GET', 'POST'))
def startSensor():
    waterButton.startSensor()
    client = app.get_mqtt_client()
    message = 'After sensor start current water level is: '+str(waterButton.getFeedingLevel())
    app.publish_message(client, message)
    return 'Water sensor is opened', 200


@bp.route('/stop-water-sensor', methods=('GET', 'POST'))
def stopSensor():
    if request.method == 'POST':
        return 'Wrong request', 404
    waterButton.stopSensor()
    client = app.get_mqtt_client()
    message = 'After sensor stop current water level is: '+str(waterButton.getFeedingLevel())
    app.publish_message(client, message)
    return 'Water sensor is closed', 200


@bp.route('/get-water-level', methods=('GET', 'POST'))
def getFeedingLevel():
    if request.method == 'POST':
        return 'Wrong request', 404
    client = app.get_mqtt_client()
    message = 'Current water level: '+str(waterButton.getFeedingLevel())
    app.publish_message(client, message)
    return f'Your water level is {waterButton.getFeedingLevel()}.', 200


@bp.route('/make-water-empty', methods=('GET', 'POST'))
def makeFeedingEmpty():
    client = app.get_mqtt_client()
    message='Current water level is: '+str(waterButton.getFeedingLevel())
    app.publish_message(client, message)
    waterButton.makeFeedingEmpty()
    return 'make water empty', 200


@bp.route('/push-water-manual', methods=('GET', 'POST'))
def pushManuel():
    client = app.get_mqtt_client()
    app.publish_message(client, 'Add water manually by incremental of 10')
    waterButton.pushManual()
    return 'Water was pushed', 200


@bp.route('/get-sensor-status', methods=('GET', 'POST'))
def getStatus():
    status = waterButton.getStatus()
    client = app.get_mqtt_client()
    message = 'Is sensor active: '+str(status)
    app.publish_message(client, message)
    if status == False:
        return 'Water sensor is inactive'
    else:
        return 'Water sensor is active'
