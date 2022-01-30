from flask import (
    Blueprint, request, jsonify
)

from db import get_db

bp = Blueprint('food', __name__, url_prefix='/food')


@bp.route('/', methods=('GET', 'POST'))
def set_food():
    if request.method == 'POST':
        food = request.form['food']

        if not food:
            return jsonify({'status': 'Food is required.'}), 403

        db = get_db()
        db.execute(
            'INSERT INTO food (level)'
            ' VALUES (?)',
            (food,)
        )
        db.commit()

    check = get_db().execute(
        'SELECT id, changed_date, level'
        ' FROM food'
        ' ORDER BY changed_date DESC'
    ).fetchone()
    return jsonify({
        'status': 'Food succesfully recorded/retrieved',
        'data': {
            'id': check['id'],
            'changed_date': check['changed_date'],
            'level': check['level']
        }
    }), 200
