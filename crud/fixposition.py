"""
  CRUD Delimitadores
  This class we can inherit to get this methods
"""

from contracts.validations import return_validation, validate_permission, validate_contract, validate_id, validate_email
from helpers.messages import messages
from helpers.order import sort_like_contracts, sort_update_like_contracts, sort_register_to_object
from helpers.constant import delimiter, jump
from contracts.fields import contracts
from helpers.constant import size_fix, delimiter


class CRUD (object):


    @staticmethod
    def create_object(current_type, line):
      obj = ""
      for word in line:
        word = str(word)
        word_length = len(word)
        spaces_need = size_fix - word_length
        word += "".join([delimiter for x in range(0, spaces_need)])
        obj += word
      return obj + '\n'
    
    @staticmethod
    def update_object(contract_type, dictionary):
      #Get a dictionary and convert it in a dimention fields format
      obj = ""
      for item in contracts[contract_type]:
        word = str(dictionary[item])
        word_length = len(word)
        spaces_need = size_fix - word_length
        word += "".join([delimiter for x in range(0, spaces_need)])
        obj += word
      return obj + '\n'

    @staticmethod
    def read_object(current_type, line):
      line = line.replace('\n', '')
      lenght = len(contracts[current_type])
      counter = 0
      obj = []
      for x in range(0, lenght + 1):
        obj.append(line[counter:counter+size_fix])
        counter+=size_fix
      obj = [x.replace(delimiter, '') for x in obj]
      obj = "".join([x + '|' for x in obj])[0:-2]
      dct = {
          'type': current_type,
          'register': obj
      }
      return sort_register_to_object(**dct)

    @staticmethod
    def get_id_of_object(line):
      #Get the line and get only the id
      return line[0:size_fix].replace(delimiter, '')
    
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

    def get_all(self, option):
      with open(self.file_path, 'r') as file:
        lines = []
        for line in file.readlines():
          obj = CRUD.read_object(self.type, line)
          if obj['status'] == 'True' or option:
            lines.append(obj)
        return lines

    @validate_id(rules='fixposition')
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
      raise ValueError("Record not found")

    @validate_contract
    def create(self, **obj):
      with open(self.file_path, 'a+') as file:
        #Get all the lines to the file to convert to ID
        if len(self.get_all(True)) == 0:
          obj['id'] = 1
        else:
          obj['id'] = int(self.get_all(True)[len(self.get_all(True)) - 1]['id']) + 1
        #Order components like fields
        sort_array = sort_like_contracts(**obj)
        #Delete the rebudand id
        #The sum +1 is sort_arrat has an id
        if len(sort_array) > len(contracts[self.type]) and 'id' in contracts[self.type]:
          sort_array.pop(0)

        file.write(CRUD.create_object(self.type, sort_array))

    @validate_id(rules='fixposition')
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

    @validate_id(rules='fixposition')
    def delete(self, id):
      dictionary = {
          'type': self.type,
          'id': id,
          'status': False
      }
      self.update(**dictionary)
