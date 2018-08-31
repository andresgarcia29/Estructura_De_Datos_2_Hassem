"""
  CRUD Delimitadores
  This class we can inherit to get this methods
"""

from contracts.validations import return_validation, validate_contract, validate_id, validate_email
from helpers.messages import messages
from helpers.order import sort_like_contracts, sort_update_like_contracts, sort_register_to_object
from helpers.constant import delimiter, jump
from contracts.fields import contracts


class CRUD (object):

    @staticmethod
    def create_object(contract_type, dictionary):
      #Get a dictionary and convert it in a dimention fields format
      string = ""
      for item in dictionary:
        lenght_string = len(str(item))
        len_id = len(str(lenght_string))
        string += str(len_id) + str(lenght_string) + str(item)
      return string + jump

    @staticmethod
    def update_object(contract_type, dictionary):
      #Get a dictionary and convert it in a dimention fields format
      string = ""
      for item in contracts[contract_type]:
        lenght_string = len(str(dictionary[item]))
        len_id = len(str(lenght_string))
        string += str(len_id) + str(lenght_string) + str(dictionary[item])
      return string + jump

    @staticmethod
    def read_object(type_contract, string):
      #Convert a dimension fields to a object
      string = string.replace('\n', '')
      object, size, position = [], 0, 0
      while position != len(string):
        current_value = int(string[size])
        position += 1
        all_size = string[position: current_value + position]
        position += current_value
        value = string[position:position + int(all_size)]
        position += int(all_size)
        size = position
        object.append(value)
      string = "".join([x + '|' for x in object])[0:-1]
      dct = {
          'type': type_contract,
          'register': string
      }
      return(sort_register_to_object(**dct))
    
    @staticmethod
    def get_id_of_object(line):
      #Get the line and get only the id
      size, position = 0, 0
      current_value = int(line[size])
      position += 1
      all_size = line[position: current_value + position]
      position += current_value
      return line[position:position + int(all_size)]

    @staticmethod
    def search_position_array_id(lines, id):
      #Search the position of id
      for i, x in enumerate(lines):
        current_id = CRUD.get_id_of_object(x)
        if int(current_id) == int(id):
          return i

    def __init__(self, *args, **kwargs):
        self.file_path = kwargs['_file']
        del kwargs['_file']

    def get_all(self):
      with open(self.file_path, 'r') as file:
        lines = []
        for line in file.readlines():
          obj = CRUD.read_object(self.type, line)
          if obj['status'] == 'True':
            lines.append(obj)
        return lines

    @validate_id(rules='dimensionfields')
    def get_one(self, id, **kwargs):
      with open(self.file_path, 'r') as file:
        for line in file:
          result = CRUD.get_id_of_object(line)
          register = CRUD.read_object(self.type, line)
          if int(result) == int(id) and register['status'] == 'True':
            dct = {
                'type': self.type,
                'register': register
            }
            return sort_register_to_object(**dct)

    @validate_contract
    #@validate_email
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

    @validate_id(rules='dimensionfields')
    @validate_contract
    def update(self, **obj):
      with open(self.file_path, 'r+') as file:
        #Find element to update
        register = self.get_one(obj['id'])
        #Save the id
        save_id = obj['id']

        del obj['type']
        del obj['id']

        #Update the new values in a current register
        for x in obj.keys():
          register[x] = obj[x]

        #Creat dimension fields object
        register = CRUD.update_object(self.type, register)

        #Get the current position of this object
        lines = file.readlines()
        current_line = self.search_position_array_id(
            lines, save_id)

        lines[int(current_line)] = register
      #Change all the text
      with open(self.file_path, 'w+') as file:
          for x in lines:
            file.write(x)

    @validate_id(rules='dimensionfields')
    def delete(self, id):
      dictionary = {
          'type': self.type,
          'id': id,
          'status': False
      }
      self.update(**dictionary)
      # with open(self.file_path, 'r+') as file:
      #   #Read all lines
      #   lines = file.readlines()
      #   #Get position of id and delete
      #   position = self.search_position_array_id(lines, id)
      #   del lines[position]
      # #Change all the text
      # with open(self.file_path, 'w+') as file:
      #     for x in lines:
      #         file.write(x)
