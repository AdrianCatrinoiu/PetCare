from db import get_db


def get_status():
    food = get_db().execute(
        'SELECT id, changed_date, level'
        ' FROM food'
        ' ORDER BY changed_date DESC'
    ).fetchone()

    water = get_db().execute(
        'SELECT id, changed_date, level'
        ' FROM water'
        ' ORDER BY changed_date DESC'
    ).fetchone()

    if food is None:
        return {'status': 'Please refill food'}

    if water is None:
        return {'status': 'Please refill water'}

    return {
        'data': {
            'food': food['level'],
            'water': water['level'],
        }
    }
