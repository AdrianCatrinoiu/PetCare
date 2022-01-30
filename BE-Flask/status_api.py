from flask import (
    Blueprint, jsonify, current_app
)

from db import get_db
import status as temp_status

bp = Blueprint('status_api', __name__, url_prefix='/status')


@bp.route('/')
def get_status_api():

    # TODO Right now default status code is 200, but the correct status code should be received
    # from bed_status.get_status().

    return temp_status.get_status(), 200
