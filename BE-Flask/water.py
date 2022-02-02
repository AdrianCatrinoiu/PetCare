from flask import (
    Blueprint, request, jsonify
)
import os,sys
from db import get_db
from db_v2 import DB

bp = Blueprint('water', __name__, url_prefix='/water')

sys.path.append(os.path.join(os.path.dirname(__file__), 'ButtonForFeeding'))
import ButtonForFeedingModel

db2 = DB()
waterButton =  ButtonForFeedingModel.ButtonForFeeding(10,5,1,'Water')

def get_blueprint():
    """Return the blueprint for the main app module"""
    return bp


@bp.route('/', methods=('GET', 'POST'))
def get_water():
    return jsonify({
        'table': 'Water',
        'rows':db2.getTableData('water')}), 200

@bp.route('/start-water-sensor',methods=('GET', 'POST'))
def startSensor():
    waterButton.startSensor()
    return 'Water sensor is opened',200

@bp.route('/stop-water-sensor',methods=('GET', 'POST'))
def stopSensor():
    waterButton.stopSensor()
    return 'Water sensor is closed',200

@bp.route('/get-water-level',methods=('GET', 'POST'))
def getFeedingLevel():
    return f'Your water level is {waterButton.getFeedingLevel()}.',200

@bp.route('/make-water-empty',methods=('GET', 'POST'))
def makeFeedingEmpty():
    waterButton.makeFeedingEmpty()
    return 'make water empty',200

@bp.route('/push-water-manual',methods=('GET', 'POST'))
def pushManuel():
    waterButton.pushManual()
    return 'Water was pushed',200

@bp.route('/get-sensor-status',methods=('GET', 'POST'))
def getStatus():
    status = waterButton.getStatus()

    if status == False:
        return 'Water sensor is inactive'
    else:
        return 'Water sensor is active'