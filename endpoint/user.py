from flask import jsonify, request
from endpoint.index import APP
from helpers.order import sort_register_to_object

from helpers.models import models

from classes.user import User
model_class = User(_file=models['user'])
url_link = '/user/'

@APP.route(url_link + 'all', methods=['GET'])
def user_get_all():
    try:
      datas = model_class.get_all()

      data = {}
      data['data'] = []

      for x in datas:
        kwargs = {
          'type': model_class.type,
          'register': x
        }
        data['data'].append(sort_register_to_object(**kwargs))

      return jsonify(status=200, data=data)
    except ValueError as error:
      return jsonify(status=500, message=error)


@APP.route(url_link + 'one/<string:id>', methods=['GET'])
def user_get_one(id):
    try:
      data = {}
      data['data'] = model_class.get_one(id, dict=True)
      return jsonify(status=200, data=data)
    except ValueError as error:
      return jsonify(status=500, message=error)


@APP.route(url_link + 'create', methods=['POST'])
def user_create():
    try:
      json = request.get_json()
      json['type'] = model_class.type

      model_class.create(**json)

      data = {}
      data['data'] = {}
      data['data']['message'] = 'User created correctly'
      return jsonify(status=200, data=data)
    except ValueError as error:
      return jsonify(status=500, message=error)


@APP.route(url_link + 'update/<string:id>', methods=['POST'])
def user_update(id):
    try:
      json = request.get_json()
      json['type'] = model_class.type
      json['id'] = id

      model_class.update(**json)

      data = {}
      data['data'] = {}
      data['data']['message'] = 'User updated correctly'
      return jsonify(status=200, data=data)
    except ValueError as error:
      return jsonify(status=500, message=error)


@APP.route(url_link + 'delete', methods=['POST'])
def user_delete():
    try:
      json = request.get_json()

      model_class.delete(json['id'])

      data = {}
      data['data'] = {}
      data['data']['message'] = 'User deleted correctly'
      return jsonify(status=200, data={})
    except ValueError as error:
      return jsonify(status=500, message=error)
