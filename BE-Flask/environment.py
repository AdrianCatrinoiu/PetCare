from flask import Blueprint, request, jsonify

import os,sys
from db import get_db
from db_v2 import DB
db2 = DB()

bp = Blueprint('environment', __name__, url_prefix='/')

sys.path.append(os.path.join(os.path.dirname(__file__), 'ButtonForThermometer'))
import ButtonForThermometerModel

thermometerButton = ButtonForThermometerModel.ButtonForThermometer(0.02)

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