from flask import (
    Blueprint, request, jsonify
)

from db import get_db

bp = Blueprint('water', __name__, url_prefix='/water')


@bp.route('/', methods=('GET', 'POST'))
def set_water():
    if request.method == 'POST':
        water = request.form['level']

        if not water:
            return jsonify({'status': 'Water is required.'}), 403

        db = get_db()
        db.execute(
            'INSERT INTO water (level)'
            ' VALUES (?)',
            (water,)
        )
        db.commit()

    check = get_db().execute(
        'SELECT id, changed_date, level'
        ' FROM water'
        ' ORDER BY changed_date DESC'
    ).fetchone()
    return jsonify({
        'status': 'Water succesfully recorded/retrieved',
        'data': {
            'id': check['id'],
            'changed_date': check['changed_date'],
            'level': check['level']
        }
    }), 200
