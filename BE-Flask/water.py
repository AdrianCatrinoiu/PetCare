import ButtonForFeedingModel
from flask import (
    Blueprint, request, jsonify
)
import os
import sys
from db import get_db
from db_v2 import DB
from app import publish_message, get_mqtt_client

bp = Blueprint('water', __name__, url_prefix='/water')

sys.path.append(os.path.join(os.path.dirname(__file__), 'ButtonForFeeding'))

db2 = DB()
waterButton = ButtonForFeedingModel.ButtonForFeeding(10, 5, 1, 'Water')


def get_blueprint():
    """Return the blueprint for the main app module"""
    return bp


@bp.route('/', methods=('GET', 'POST'))
def get_water():
    client = get_mqtt_client()
    publish_message(client, 'Get water history')
    return jsonify({
        'table': 'Water',
        'rows': db2.getTableData('water')}), 200


@bp.route('/start-water-sensor', methods=('GET', 'POST'))
def startSensor():
    waterButton.startSensor()
    client = get_mqtt_client()
    publish_message(client, 'Start water sensor')
    return 'Water sensor is opened', 200


@bp.route('/stop-water-sensor', methods=('GET', 'POST'))
def stopSensor():
    waterButton.stopSensor()
    client = get_mqtt_client()
    publish_message(client, 'Stop water sensor')
    return 'Water sensor is closed', 200


@bp.route('/get-water-level', methods=('GET', 'POST'))
def getFeedingLevel():
    client = get_mqtt_client()
    message = 'Get water level: '+str(waterButton.getFeedingLevel())
    publish_message(client, message)
    return f'Your water level is {waterButton.getFeedingLevel()}.', 200


@bp.route('/make-water-empty', methods=('GET', 'POST'))
def makeFeedingEmpty():
    client = get_mqtt_client()
    publish_message(client, 'Make current water empty')
    waterButton.makeFeedingEmpty()
    return 'make water empty', 200


@bp.route('/push-water-manual', methods=('GET', 'POST'))
def pushManuel():
    client = get_mqtt_client()
    publish_message(client, 'Add water manually by incremental of 10')
    waterButton.pushManual()
    return 'Water was pushed', 200
