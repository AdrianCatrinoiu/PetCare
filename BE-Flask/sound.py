from flask import (
    Blueprint, request, jsonify
)
import os,sys
from db import get_db

bp = Blueprint('timer', __name__, url_prefix='/timer')

sys.path.append(os.path.join(os.path.dirname(__file__), 'TimerForSleeping'))
import TimerForSleepingModel

timer = TimerForSleepingModel.Timer(60)

@bp.route('/make-silence', methods=('GET', 'POST'))
def set_silence():
    timer.makeSilence()
    return 200

@bp.route('/make-noise', methods=('GET', 'POST'))
def set_silence():
    timer.makeNoise()
    return 200

@bp.route('/start-timer', methods=('GET', 'POST'))
def start_timer():
    timer.startTimer()
    return 200