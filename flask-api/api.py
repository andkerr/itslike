from flask import Blueprint
from random import randrange

from .db import get_db

bp = Blueprint('api', __name__, url_prefix="")

@bp.route('/')
def index():
    return bp.send_static_file('index.html')

@bp.route('api/hello')
def hello():
    return {'response':"Flask is connected. We are live!!"}

@bp.route('api/random')
def return_random():
    db = get_db()

    companies = db.execute(
        'SELECT * FROM companies'
    ).fetchall()

    objects = db.execute(
        'SELECT * FROM objects'
    ).fetchall()

    prev_indices = db.execute(
        'SELECT * FROM prev_indices'
    ).fetchone()

    company_index = randrange(len(companies))
    obj_index = randrange(len(objects))
    prev_company_index = None
    prev_obj_index = None

    if prev_indices is not None:
        prev_company_index = prev_indices["prev_company"]
        prev_obj_index = prev_indices["prev_obj"]

        while company_index == prev_company_index:
            company_index = randrange(len(companies))

        while obj_index == prev_obj_index:
            obj_index = randrange(len(objects))

    company = companies[company_index]["company"]
    obj = objects[obj_index]["obj"]

    if prev_indices is not None:
        db.execute(
            'UPDATE prev_indices'
            ' SET prev_company = (?), prev_obj = (?)'
            ' WHERE id == 1', (company_index, obj_index,)
        )
        db.commit()
    else:
        db.execute(
            'INSERT INTO prev_indices (prev_company, prev_obj)'
            ' VALUES (?, ?)', (company_index, obj_index,)
        )
        db.commit()

    return {
        'rand1': company,
        'rand2': obj
    }