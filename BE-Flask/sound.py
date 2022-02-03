from flask import (
    Blueprint, request, jsonify
)
import os,sys
import app
bp = Blueprint('timer', __name__, url_prefix='/')

sys.path.append(os.path.join(os.path.dirname(__file__), 'TimerForSleeping'))
import TimerForSleepingModel

timer = TimerForSleepingModel.Timer(60)

@bp.route('/make-silence', methods=('GET', 'POST'))
def makeSilence():
    timer.makeSilence()
    client = app.get_mqtt_client()
    message = 'Make silence initiated'
    app.publish_message(client, message)
    return 'Make silence',200

@bp.route('/make-noise', methods=('GET', 'POST'))
def makeNoise():
    timer.makeNoise()
    client = app.get_mqtt_client()
    message = 'Make noise initiated'
    app.publish_message(client, message)
    return 'Make noise',200

@bp.route('/start-timer-for-silence', methods=('GET', 'POST'))
def startTimer():
    timer.startTimer()
    client = app.get_mqtt_client()
    message = 'Start timer initiated'
    app.publish_message(client, message)
    return 'Start timer to making silence',200