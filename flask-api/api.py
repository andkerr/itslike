from flask import Blueprint
from random import randrange

from .db import get_db

bp = Blueprint('api', __name__, url_prefix="")

@bp.route('/hello')
def hello():
    return {'response':"Flask is connected. We are live!!"}

prev_company_index = None
prev_object_index = None

@bp.route('/random')
def return_random():
    db = get_db()

    companies = db.execute(
        'SELECT * FROM companies'
    ).fetchall()

    objects = db.execute(
        'SELECT * FROM objects'
    ).fetchall()

    company_index = randrange(len(companies))
    while company_index == prev_company_index:
        company_index = randrange(len(companies))

    obj_index = randrange(len(objects))
    while obj_index == prev_object_index:
        obj_index = randrange(len(objects))

    company = companies[company_index]["company"]
    obj = objects[obj_index]["obj"]

    return {
        'rand1': company,
        'rand2': obj
    }