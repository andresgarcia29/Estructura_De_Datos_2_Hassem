"""
  CRUD
  This class we can inherit to get this methods
"""

from contracts.validations import return_validation, validate_contract, validate_id, validate_email
from helpers.messages import messages
from helpers.order import sort_like_contracts, sort_update_like_contracts, sort_register_to_object
from helpers.constant import delimiter, jump

class CRUD (object):

    @staticmethod
    def converto_to_text(sort_array):
        #Convert array to format text
        text = ""
        for x in sort_array:
            text += str(x) + delimiter
        text = text[0: len(text) - 1] + jump
        return text

    @staticmethod
    def search_position_array_id(lines, id):
      #Search the position of id
        for i, x in enumerate(lines):
            if x.split(delimiter)[0] == str(id):
                return i

    def __init__(self, *args, **kwargs):
        self.file_path = kwargs['_file']
        del kwargs['_file']

    def get_all(self):
      with open(self.file_path, 'r') as file:
        lines = []
        for line in file:
          lines.append(line)
        return lines

    @validate_id
    def get_one(self, id, **kwargs):
      with open(self.file_path, 'r') as file:
        for line in file:
          if int(line.split(delimiter)[0]) == int(id):
            file.close()
            if kwargs.get('dict'):
                dct = {
                    'type': self.type,
                    'register': line
                }
                return sort_register_to_object(**dct)
            else:
                return line

    @validate_contract
    @validate_email
    def create(self, **obj):
      with open(self.file_path, 'a+') as file:
        #Get all the lines to the file to convert to ID
        self.id = [x for x in open(self.file_path).readlines()]
        self.id = str(int(self.id[len(self.id) - 1].split(delimiter)[0]) + 1)
        #Assign ID
        obj['id'] = self.id
        #Order components like fields
        sort_array = sort_like_contracts(**obj)
        #Prepair text to insert
        text = ""
        for x in sort_array:
          text += str(x) + delimiter
        text = text[0: len(text) - 1] + jump
        #Insert text in a file

        file.write(text)

    @validate_id
    @validate_contract
    @validate_email
    def update(self, **obj):
      with open(self.file_path, 'r+') as file:
        #Find element to update
        register = self.get_one(obj['id'])
        #Delete the primary object
        del obj['id']
        #Sort and update the exactly fields
        kwargs = {}
        kwargs['obj'] = obj
        kwargs['register'] = register
        register = sort_update_like_contracts(**kwargs)
        #Prepair string to change in array
        register = self.converto_to_text(register)
        #Delete a line and insert the line
        lines = file.readlines()
        current_line = self.search_position_array_id(lines, register.split(delimiter)[0])
        lines[int(current_line)] = register
      #Change all the text
      with open(self.file_path, 'w+') as file:
          for x in lines:
            file.write(x)

    @validate_id
    def delete(self, id):
      with open(self.file_path, 'r+') as file:
        #Read all lines
        lines = file.readlines()
        #Get position of id and delete
        position = self.search_position_array_id(lines, id)
        del lines[position]
      #Change all the text
      with open(self.file_path, 'w+') as file:
          for x in lines:
              file.write(x)
