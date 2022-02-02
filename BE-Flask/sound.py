from flask import (
    Blueprint, request, jsonify
)
import os,sys
from db import get_db

bp = Blueprint('timer', __name__, url_prefix='/')

sys.path.append(os.path.join(os.path.dirname(__file__), 'TimerForSleeping'))
import TimerForSleepingModel

timer = TimerForSleepingModel.Timer(60)

@bp.route('/make-silence', methods=('GET', 'POST'))
def makeSilence():
    timer.makeSilence()
    return 'Make silence',200

@bp.route('/make-noise', methods=('GET', 'POST'))
def makeNoise():
    timer.makeNoise()
    return 'Make noise',200

@bp.route('/start-timer-for-silence', methods=('GET', 'POST'))
def startTimer():
    timer.startTimer()
    return 'Start timer to making silence',200