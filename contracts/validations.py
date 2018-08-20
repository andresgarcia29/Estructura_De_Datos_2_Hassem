"""
  Validate contract
"""

from contracts.fields import contracts
from helpers.messages import messages

remove_information_objects = ['type']

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
        if x not in contract and x != 'id':
            return False
    return True


def validate_contract(func):
    #Wrapper to check the contract is perfectly
    def check_contract(*args, **kwargs):
        #Call to validation function and return true or false and a message
        if return_validation(**kwargs):
            raise ValueError(messages['success']['contract'])
            return func(*args, **kwargs)
        else:
            raise ValueError(messages['error']['contract'])
    return check_contract


def validate_id(func):
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
                if x.split('|')[0] == str(current_id):
                    flag = True
        if flag:
            return func(*args, **kwargs)
        else:
            #No se encontro el ID
            raise ValueError("Can't find the id")
    return check_contract


def validate_email(func):
    #Wrapper to check the contract is perfectly
    def check_contract(*args, **kwargs):
        #Call to validation function and return true or false and a message
        if 'email' not in kwargs.keys():
            return True

        import re

        addressToVerify = kwargs['email']
        regex = "^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$"
        match = re.match(regex,
                            addressToVerify)

        if match == None:
            raise ValueError('Email not good format')
        else:
            return True
    return check_contract
