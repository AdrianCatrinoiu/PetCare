from flask import Blueprint, request, jsonify

import os,sys
from db_v2 import DB
db2 = DB()
import app
import json
bp = Blueprint('environment', __name__, url_prefix='/')

sys.path.append(os.path.join(os.path.dirname(__file__), 'ButtonForThermometer'))
import ButtonForThermometerModel

thermometerButton = ButtonForThermometerModel.ButtonForThermometer()

f = open('paramConfig.json')
parameterConfig = json.load(f)
tempReadings = parameterConfig['thermometer']['thermometerReadings']
indexTemp = 0

@bp.route('/get-temperature', methods=['GET','POST'])
def get_temperature():
    client = app.get_mqtt_client()
    app.publish_message(client, 'Get temperature history')
    return jsonify({
        'table': 'Temperature',
        'rows':db2.getTableData('temperature')}), 200

@bp.route('/start-thermometer',methods=('GET', 'POST'))
def startSensor():
    thermometerButton.startSensor()
    client = app.get_mqtt_client()
    app.publish_message(client, 'Start thermometer')
    return 'Thermometer started',200

@bp.route('/stop-thermometer',methods=('GET', 'POST'))
def stopSensor():
    thermometerButton.stopSensor()
    client = app.get_mqtt_client()
    app.publish_message(client, 'Stop thermometer')
    return 'Thermometer stopped',200

@bp.route('/get-current-temperature',methods=('GET', 'POST'))
def getFeedingLevel():
    temperature = thermometerButton.getTemp()
    client = app.get_mqtt_client()
    message = 'Current temperature is: '+str(temperature)
    app.publish_message(client, message)
    return f'Current temperature is: { temperature }C',200

@bp.route('/set-current-temperature',methods=('GET', 'POST'))
def setFeedingLevel():
    client = app.get_mqtt_client()
    if request.method == 'POST':
        if 'temp' in request.form:
            data = request.form['temp']
            thermometerButton.setTempHardware(data)
            temperature = thermometerButton.setTempHardware(data)
            return f'Current temperature is: { temperature }C',200
        else:
            global indexTemp
            if indexTemp == len(tempReadings):
                indexTemp = 0
            temperature = thermometerButton.setTempHardware(tempReadings[indexTemp])
            print(tempReadings[indexTemp])
            indexTemp = indexTemp + 1
            return f'Current temperature is: { temperature }C',200
    else:
        message = 'Current temperature is wrong'
        app.publish_message(client, message)
        return 'Wrong request',404

@bp.route('/get-sensor-status',methods=('GET', 'POST'))
def getStatus():
    status = thermometerButton.getStatus()
    client = app.get_mqtt_client()
    message = 'Is sensor active: '+str(status)
    if status == False:
        return 'Thermometer is inactive'
    else:
        return 'Thermometer is active'
