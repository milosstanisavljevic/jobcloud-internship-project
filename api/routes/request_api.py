import db
from flask import jsonify, Blueprint


request_api = Blueprint('request_api', __name__)


def get_blueprint():
    return request_api


@request_api.route('/request', methods=['GET'])
def get_job_ads():
    return jsonify(db.get_items())
    # ceo js objekat


@request_api.route('/request/job_address/<string:address>', methods=['GET'])
def get_job_ads_per_city(address):
    print(address)
    key = 'job_address'
    index = 'job_address-index'
    return jsonify(db.db_get_item_index(index, key, address))


@request_api.route('/request/employer_name/<string:employer>', methods=['GET'])
def get_job_ads_per_employer(employer):
    print(employer)
    key = 'employer_name'
    index = 'employer_name-index'
    return jsonify(db.db_get_item_index(index, key, employer))


@request_api.route('/request/publishing_date/<string:publish_date>', methods=['GET'])
def get_job_ads_per_certain_date(publish_date):
    print(publish_date)
    key = 'publishing_date'
    index = 'publishing_date-index'
    return jsonify(db.db_get_item_index(index, key, publish_date))
