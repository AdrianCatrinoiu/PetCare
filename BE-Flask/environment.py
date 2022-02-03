from flask import Blueprint, request, jsonify

import os,sys
from db import get_db
from db_v2 import DB
db2 = DB()

bp = Blueprint('environment', __name__, url_prefix='/')

sys.path.append(os.path.join(os.path.dirname(__file__), 'ButtonForThermometer'))
import ButtonForThermometerModel

thermometerButton = ButtonForThermometerModel.ButtonForThermometer(5,23)

@bp.route('/get-temperature', methods=['GET','POST'])
def get_temperature():
    return jsonify({
        'table': 'Temperature',
        'rows':db2.getTableData('temperature')}), 200

@bp.route('/start-thermometer',methods=('GET', 'POST'))
def startSensor():
    thermometerButton.startSensor()
    return 'Thermometer started',200

@bp.route('/stop-thermometer',methods=('GET', 'POST'))
def stopSensor():
    thermometerButton.stopSensor()
    return 'Thermometer stopped',200

@bp.route('/get-current-temperature',methods=('GET', 'POST'))
def getFeedingLevel():
    temperature = thermometerButton.getTemp()
    return f'Current temperature is: { temperature }C',200

@bp.route('/set-current-temperature',methods=('GET', 'POST'))
def setFeedingLevel():
    if request.method == 'POST':
        data = request.form['temp']
        thermometerButton.setTempHardware(data)
        temperature = thermometerButton.setTempHardware(data)
        return f'Current temperature is: { temperature }C',200
    else:
        return 'Wrong request',404

@bp.route('/get-sensor-status',methods=('GET', 'POST'))
def getStatus():
    status = thermometerButton.getStatus()

    if status == False:
        return 'Thermometer is inactive'
    else:
        return 'Thermometer is active'
