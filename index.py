from classes.user import User
from helpers.models import models
from helpers.order import sort_register_to_object

user_object = {
  'type': 'user',
  'username': 'Andres',
  'password': 'sdfsdfsdf'
}

user = User(_file=models['user'])
# user.create(**user_object)
s = user.get_one(0, dict=False)
print(s)
