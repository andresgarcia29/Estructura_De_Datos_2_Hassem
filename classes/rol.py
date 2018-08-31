from crud.dimensionfields import CRUD
from contracts.validations import validate_id
from helpers.models import models


class Rol(CRUD):

    def __init__(self, *args, **kwargs):
      super(Rol, self).__init__(*args, **kwargs)
      self.type = 'rol'

    @validate_id(rules='dimensionfields')
    def delete(self, id):
      with open(models['user'], 'r+') as file:
        print(file.read())
        for line in file.readlines():
          print(line)
          print(CRUD.read_object(line))
