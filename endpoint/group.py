from flask import jsonify, request
from endpoint.index import APP
from helpers.order import sort_register_to_object
from helpers.messages import make_message_to_success, make_message_to_error

from helpers.headers import get_secret_role

from helpers.models import models

from classes.group import Group
model_class = Group(_file=models['group'])
name_class = 'group'
url_link = '/' + name_class + '/'


@APP.route(url_link + 'get', methods=['GET'], endpoint=name_class + 'get_all')
@get_secret_role([1, 2, 3])
def get_all():
    try:
      datas = model_class.get_all(False)

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
@get_secret_role([1, 2, 3])
def get_one(id):
    try:
      data = {}
      data['data'] = model_class.get_one(id, dict=True)
      return jsonify(status=200, data=data)
    except ValueError as error:
      return jsonify(status=500, message=make_message_to_error(name_class, 'get one', error))


@APP.route(url_link + 'create', methods=['POST'], endpoint=name_class + 'create')
@get_secret_role([1, 2, 3])
def create():
    try:
      json = request.get_json()
      json['type'] = model_class.type

      model_class.create(**json)

      return jsonify(status=200, data=make_message_to_success(name_class, 'create'))
    except ValueError as error:
      return jsonify(status=500, message=make_message_to_error(name_class, 'create', error))


@APP.route(url_link + 'update/<string:id>', methods=['POST'], endpoint=name_class + 'update')
@get_secret_role([1, 2, 3])
def update(id):
    try:
      json = request.get_json()
      json['type'] = model_class.type
      json['id'] = id

      model_class.update(**json)

      return jsonify(status=200, data=make_message_to_success(name_class, 'update'))
    except ValueError as error:
      return jsonify(status=500, message=make_message_to_error(name_class, 'update', error))


@APP.route(url_link + 'delete', methods=['POST'], endpoint=name_class + 'delete')
@get_secret_role([1, 2, 3])
def delete():
    try:
      json = request.get_json()

      model_class.delete(json['id'])

      return jsonify(status=200, data=make_message_to_success(name_class, 'delete'))
    except ValueError as error:
      return jsonify(status=500, message=make_message_to_error(name_class, 'delete', error))


@APP.route(url_link + 'delete/fisic', methods=['POST'], endpoint=name_class + 'delete_fisic')
@get_secret_role([1, 2, 3])
def delete_fisic():
    try:
      json = request.get_json()

      model_class.delete_fisic(json['id'])

      return jsonify(status=200, data=make_message_to_success(name_class, 'delete'))
    except ValueError as error:
      return jsonify(status=500, message=make_message_to_error(name_class, 'delete', error))
