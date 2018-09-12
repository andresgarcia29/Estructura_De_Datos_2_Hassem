from crud.fixposition import CRUD
from classes.offer import Offer
from contracts.validations import return_validation, validate_permission, validate_contract, validate_id, validate_email
from helpers.models import models

class Period(CRUD):

    def __init__(self, *args, **kwargs):
      super(Period, self).__init__(*args, **kwargs)
      self.type = 'period'
      self.offer_class = Offer(_file=models['offer'])

    @validate_id(rules='fixposition')
    def delete(self, id):
      array = self.offer_class.get_group_by_periods(id)
      print(array)
      print(len(array))
      if len(array) == 0:
        dictionary = {
            'type': self.type,
            'id': id,
            'status': False
        }
        self.update(**dictionary)
      else:
        raise ValueError('The period has at leat one group')

    @validate_id(rules='fixposition')
    def delete_fisic(self, id):
      array = self.offer_class.get_group_by_periods(id)
      if len(array) == 0:
        with open(self.file_path, 'r+') as file:
          #Read all lines
          lines = file.readlines()
          #Get position of id and delete
          current = self.get_one(id)
          if current['status'] == 'False':
            raise ValueError('The register is desactivated')
          position = self.search_position_array_id(lines, id)
          del lines[position]
        #Change all the text
        with open(self.file_path, 'w+') as file:
            for x in lines:
                file.write(x)
      else:
        raise ValueError('The period has at leat one group')
