from flask import jsonify, request
from endpoint.index import APP
from helpers.order import sort_register_to_object
from helpers.messages import make_message_to_success, make_message_to_error

from helpers.models import models

from classes.user import User
model_class = User(_file=models['user'])
name_class = 'user'
url_link = '/' + name_class + '/'

@APP.route(url_link + 'get', methods=['GET'], endpoint=name_class + 'get_all')
def get_all():
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
      return jsonify(status=500, message=make_message_to_error(name_class, 'get', error))


@APP.route(url_link + 'get/<string:id>', methods=['GET'], endpoint=name_class + 'get_one')
def get_one(id):
    try:
      data = {}
      data['data'] = model_class.get_one(id, dict=True)
      return jsonify(status=200, data=data)
    except ValueError as error:
      return jsonify(status=500, message=make_message_to_error(name_class, 'get one', error))


@APP.route(url_link + 'create', methods=['POST'], endpoint=name_class + 'create')
def create():
    try:
      json = request.get_json()
      json['type'] = model_class.type

      model_class.create(**json)

      return jsonify(status=200, data=make_message_to_success(name_class, 'create', 'success'))
    except ValueError as error:
      return jsonify(status=500, message=make_message_to_error(name_class, 'create', error))


@APP.route(url_link + 'update/<string:id>', methods=['POST'], endpoint=name_class + 'update')
def update(id):
    try:
      json = request.get_json()
      json['type'] = model_class.type
      json['id'] = id

      model_class.update(**json)

      return jsonify(status=200, data=make_message_to_success(name_class, 'update', 'success'))
    except ValueError as error:
      return jsonify(status=500, message=make_message_to_error(name_class, 'update', error))


@APP.route(url_link + 'delete', methods=['POST'], endpoint=name_class + 'delete')
def delete():
    try:
      json = request.get_json()

      model_class.delete(json['id'])

      return jsonify(status=200, data=make_message_to_success(name_class, 'delete', 'success'))
    except ValueError as error:
      return jsonify(status=500, message=make_message_to_error(name_class, 'delete', error))
