from flask import (
    Blueprint, request, jsonify
)
import os,sys
from db import get_db
from db_v2 import DB

bp = Blueprint('food', __name__, url_prefix='/food')
db2 = DB()

sys.path.append(os.path.join(os.path.dirname(__file__), 'ButtonForFeeding'))
import ButtonForFeedingModel

foodButton = ButtonForFeedingModel.ButtonForFeeding(25,20,2,'Food')



@bp.route('/', methods=('GET', 'POST'))
def get_food():
    return jsonify({
        'table': 'Food',
        'rows':db2.getTableData('food')}), 200


@bp.route('/start-food-sensor',methods=('GET', 'POST'))
def startSensor():
    foodButton.startSensor()
    return 'Food sensor is opened',200

@bp.route('/stop-food-sensor',methods=('GET', 'POST'))
def stopSensor():
    foodButton.stopSensor()
    return 'Food sensor is closed',200

@bp.route('/get-food-level',methods=('GET', 'POST'))
def getFeedingLevel():
    return f'Your food level is {foodButton.getFeedingLevel()}.',200

@bp.route('/make-food-empty',methods=('GET', 'POST'))
def makeFeedingEmpty():
    foodButton.makeFeedingEmpty()
    return 'make food empty',200

@bp.route('/push-food-manual',methods=('GET', 'POST'))
def makeFeedingEmpty():
    foodButton.pushManual()
    return 'Food was pushed',200