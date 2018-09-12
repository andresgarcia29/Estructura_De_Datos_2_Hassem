"""
  Validate contract
"""

from contracts.fields import contracts
from helpers.messages import messages
from helpers.constant import delimiter, size_fix
from helpers.order import sort_register_to_object
from helpers.models import models

remove_information_objects = ['type']


def get_id_of_object(line):
      #Get the line and get only the id
      size, position = 0, 0
      current_value = int(line[size])
      position += 1
      all_size = line[position: current_value + position]
      position += current_value
      return line[position:position + int(all_size)]


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


# !--------------- Start with validations only ---------------!

def return_validation(**kwargs):
    #Get the contract type
    type_contract = kwargs['type']

    #Remove to dependencies fields
    for x in remove_information_objects:
        del kwargs[x]

    #Get current items and the contract to check them
    items = list(kwargs.keys())
    contract = contracts[type_contract]

    items = list(kwargs.keys())
    #If not find at least one the contract is broke
    for x in items:
        print(items)
        if x not in contract and x != 'id' and x != 'status':
            return False
    return True


def validate_contract(func):
    #Wrapper to check the contract is perfectly
    def check_contract(*args, **kwargs):
        #Call to validation function and return true or false and a message
        if return_validation(**kwargs):
            return func(*args, **kwargs)
        else:
            raise ValueError(messages['error']['contract'])
    return check_contract


def validate_id(rules):
    def validate_id_function(func):
        #Wrapper to check the contract is perfectly
        def check_contract(*args, **kwargs):
            #Call to validation function and return true or false and a message
            file = args[0].file_path
            try:
                current_id = args[1]
            except:
                current_id = kwargs['id']
            with open(file, 'r+') as file:
                flag = False
                for x in file.readlines():
                    if rules == 'delimiters':
                        if x.split(delimiter)[0] == str(current_id):
                            flag = True
                    elif rules == 'dimensionfields':
                        if str(get_id_of_object(x)) == str(current_id):
                            flag = True
                    elif rules == 'fixposition':
                        if x[0:size_fix].replace(delimiter, '') == str(current_id):
                            flag = True
            if flag:
                return func(*args, **kwargs)
            else:
                #No se encontro el ID
                raise ValueError("Can't find the id")
        return check_contract
    return validate_id_function


def validate_rol(rules):
    def validate_id_function(func):
        #Wrapper to check the contract is perfectly
        def check_contract(*args, **kwargs):
            #Call to validation function and return true or false and a message
            rol = kwargs['rol']
            file_name=args[0].file_path

            flag = False

            with open(models['rol'], 'r+') as file:
                print(file_name)
                for line in file.readlines():
                    obj = read_object('rol', line)
                    if str(obj['id']) == str(rol):
                        flag = True

            if flag:
                return func(*args, **kwargs)
            else:
                #Can't find the id
                raise ValueError("Can't find the role")
        return check_contract
    return validate_id_function

def validate_email(func):
    #Wrapper to check the contract is perfectly
    def check_contract(*args, **kwargs):
        #Call to validation function and return true or false and a message
        if 'email' not in kwargs.keys():
            return True

        import re

        address_to_verify = kwargs['email']
        regex = r"^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$"
        match = re.match(regex,
                            address_to_verify)
        if len([i for i, a in enumerate(address_to_verify) if a == '.']) > 0 and len([i for i, a in enumerate(address_to_verify) if a == '.']) < 2:
            if len(address_to_verify.split('.')[-1]) > 1 and len(address_to_verify.split('.')[-1]) < 4:
                pass
            else:
                print("Error 1")
                match = None
        else:
            print("Error 2")
            match = None

        if match == None:
            raise ValueError('Email not good format')
        else:
            return func(*args, **kwargs)
    return check_contract


def validate_permission(rules, rol):
    rules = [str(x) for x in rules]

    flag = False

    with open(models['rol'], 'r+') as file:
        for line in file.readlines():
            obj = read_object('rol', line)
            if str(rol) in rules:
                flag = True

    if flag:
        return True
    else:
        #Can't find the id
        raise ValueError("You don't have permission to do this")
