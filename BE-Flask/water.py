from flask import (
    Blueprint, request, jsonify
)
import os,sys
from db import get_db

bp = Blueprint('water', __name__, url_prefix='/water')

sys.path.append(os.path.join(os.path.dirname(__file__), 'ButtonForFeeding'))
import ButtonForFeedingModel

waterButton =  ButtonForFeedingModel.ButtonForFeeding(10,5,1,'Water')

@bp.route('/', methods=('GET', 'POST'))
def set_water():
    if request.method == 'POST':
        water = request.form['level']

        if not water:
            return jsonify({'status': 'Water is required.'}), 403

        db = get_db()
        db.execute(
            'INSERT INTO water (level)'
            ' VALUES (?)',
            (water,)
        )
        db.commit()

    check = get_db().execute(
        'SELECT id, changed_date, level'
        ' FROM water'
        ' ORDER BY changed_date DESC'
    ).fetchone()
    return jsonify({
        'status': 'Water succesfully recorded/retrieved',
        'data': {
            'id': check['id'],
            'changed_date': check['changed_date'],
            'level': check['level']
        }
    }), 200

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