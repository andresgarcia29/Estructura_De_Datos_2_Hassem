from crud.dimensionfields import CRUD
from contracts.validations import validate_contract, validate_rol
from helpers.order import sort_like_contracts
from contracts.fields import contracts


class User(CRUD):

    def __init__(self, *args, **kwargs):
      super(User, self).__init__(*args, **kwargs)
      self.type = 'user'

    def login(self, **obj):
      with open(self.file_path, 'a+') as file:
        register = self.get_all(False)
        for user in register:
          if obj['name'] == user['name']:
            if obj['password'] == user['password']:
              return user['rol']
        raise ValueError('User and password not correctly')

    @validate_contract
    @validate_rol(rules='dimensionfields')
    def create(self, **obj):
      with open(self.file_path, 'a+') as file:
        #Get all the lines to the file to convert to ID
        if len(self.get_all(True)) == 0:
          obj['id'] = 1
        else:
          obj['id'] = int(self.get_all(True)[len(self.get_all(True)) - 1]['id']) + 1

        obj['status'] = True

        #Order components like fields
        sort_array = sort_like_contracts(**obj)
        #Delete the rebudand id
        if len(sort_array) > len(contracts[self.type]):
          sort_array.pop(0)

        file.write(CRUD.create_object(self.type, sort_array))
