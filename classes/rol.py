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
        flag = False
        for line in file.readlines():
          obj = CRUD.read_object('user', line)
          if str(obj['rol']) == str(id):
            flag = True
      if flag == True:
        raise ValueError('This role has associate at least one user')
      else:
        CRUD.delete(self, id)
