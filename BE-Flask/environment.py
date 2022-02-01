from flask import Blueprint, request, jsonify

from db import get_db

bp = Blueprint('environment', __name__)


@bp.route('/temperature', methods=['POST'])
def set_temperature():
    temp = request.form['temp']
    error = None

    if not temp:
        return jsonify({'status': 'Temp is required.'}), 403

    print(temp)
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
