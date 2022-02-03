from flask import (
    Blueprint, request, jsonify
)
import os
import sys
from db_v2 import DB
import app
bp = Blueprint('food', __name__, url_prefix='/food')
db2 = DB()

sys.path.append(os.path.join(os.path.dirname(__file__), 'ButtonForFeeding'))
import ButtonForFeedingModel

foodButton = ButtonForFeedingModel.ButtonForFeeding(25, 20, 2, 'Food')


@bp.route('/', methods=('GET', 'POST'))
def get_food():
    client = app.get_mqtt_client()
    app.publish_message(client, 'Get food history')
    return jsonify({
        'table': 'Food',
        'rows': db2.getTableData('food')}), 200


@bp.route('/start-food-sensor', methods=('GET', 'POST'))
def startSensor():
    foodButton.startSensor()
    client = app.get_mqtt_client()
    app.publish_message(client, 'Start food sensor')
    return 'Food sensor is opened', 200


@bp.route('/stop-food-sensor', methods=('GET', 'POST'))
def stopSensor():
    if request.method == 'POST':
        return 'Wrong request', 404
    foodButton.stopSensor()
    client = app.get_mqtt_client()
    app.publish_message(client, 'Stop food sensor')
    return 'Food sensor is closed', 200


@bp.route('/get-food-level', methods=('GET', 'POST'))
def getFeedingLevel():
    if request.method == 'POST':
        return 'Wrong request', 404
    client = app.get_mqtt_client()
    message = 'Current food level: '+str(foodButton.getFeedingLevel())
    app.publish_message(client, message)
    return f'Your food level is {foodButton.getFeedingLevel()}.', 200


@bp.route('/make-food-empty', methods=('GET', 'POST'))
def makeFeedingEmpty():
    foodButton.makeFeedingEmpty()
    client = app.get_mqtt_client()
    app.publish_message(client, 'Make current food empty')
    return 'make food empty', 200


@bp.route('/push-food-manual', methods=('GET', 'POST'))
def pushManuel():
    foodButton.pushManual()
    client = app.get_mqtt_client()
    app.publish_message(client, 'Add water manually by incremental of 25')
    return 'Food was pushed', 200


@bp.route('/get-sensor-status', methods=('GET', 'POST'))
def getStatus():
    status = foodButton.getStatus()
    client = app.get_mqtt_client()
    message = 'Is sensor active: '+str(status)
    app.publish_message(client, message)
    if status == False:
        return 'Food sensor is inactive'
    else:
        return 'Food sensor is active'
