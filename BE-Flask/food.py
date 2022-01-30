from flask import (
    Blueprint, request, jsonify
)
import os,sys
from db import get_db

bp = Blueprint('food', __name__, url_prefix='/food')

sys.path.append(os.path.join(os.path.dirname(__file__), 'ButtonForFeeding'))
import ButtonForFeedingModel

foodButton = ButtonForFeedingModel.ButtonForFeeding(25,20,2,'Food')



@bp.route('/', methods=('GET', 'POST'))
def set_food():
    if request.method == 'POST':
        food = request.form['food']

        if not food:
            return jsonify({'status': 'Food is required.'}), 403

        db = get_db()
        db.execute(
            'INSERT INTO food (level)'
            ' VALUES (?)',
            (food,)
        )
        db.commit()

    check = get_db().execute(
        'SELECT id, changed_date, level'
        ' FROM food'
        ' ORDER BY changed_date DESC'
    ).fetchone()
    return jsonify({
        'status': 'Food succesfully recorded/retrieved',
        'data': {
            'id': check['id'],
            'changed_date': check['changed_date'],
            'level': check['level']
        }
    }), 200


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