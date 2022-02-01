from flask import (
    Blueprint, request, jsonify
)

import os,sys
from db import get_db

bp = Blueprint('environment', __name__, url_prefix='/')

sys.path.append(os.path.join(os.path.dirname(__file__), 'ButtonForThermometer'))
import ButtonForThermometerModel

thermometerButton = ButtonForThermometerModel.ButtonForThermometer(0.02)

@bp.route('/set-temperature', methods=['GET','POST'])
def set_temperature():
    if request.method == 'POST':
        temp = request.form['temp']
        error = None

        if not temp:
            return jsonify({'status': 'Temp is required.'}), 403

        thermometerButton.setTempHardware(temp)
        db = get_db()
        db.execute(
            'INSERT INTO temperature (level)'
            ' VALUES (?)',
            (temp,)
        )
        db.commit()

        check = get_db().execute(
            'SELECT id, timestamp, level'
            ' FROM temperature'
            ' ORDER BY timestamp DESC'
        ).fetchone()
        return jsonify({
            'status': 'Temperature succesfully recorded',
            'data': {
                'id': check['id'],
                'timestamp': check['timestamp'],
                'level': check['level']
            }
        }), 200

@bp.route('/start-thermometer',methods=('GET', 'POST'))
def startSensor():
    thermometerButton.startSensor()
    return 'Thermometer started',200

@bp.route('/stop-thermometer',methods=('GET', 'POST'))
def stopSensor():
    thermometerButton.stopSensor()
    return 'Thermometer stopped',200

@bp.route('/get-temperature',methods=('GET', 'POST'))
def getFeedingLevel():
    temperature = thermometerButton.getTemp()
    return f'Current temperature is: { temperature }C',200