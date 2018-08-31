from crud.dimensionfields import CRUD
from contracts.validations import validate_contract, validate_rol
from helpers.order import sort_like_contracts
from contracts.fields import contracts


class User(CRUD):

    def __init__(self, *args, **kwargs):
      super(User, self).__init__(*args, **kwargs)
      self.type = 'user'

    @validate_contract
    @validate_rol(rules='dimensionfields')
    def create(self, **obj):
      with open(self.file_path, 'a+') as file:
        #Get all the lines to the file to convert to ID
        try:
          obj['id'] = int(self.get_all()[len(self.get_all()) - 1]['id']) + 1
        except:
          obj['id'] = 1

        obj['status'] = True

        #Order components like fields
        sort_array = sort_like_contracts(**obj)
        #Delete the rebudand id
        if len(sort_array) > len(contracts[self.type]):
          sort_array.pop(0)

        file.write(CRUD.create_object(self.type, sort_array))
