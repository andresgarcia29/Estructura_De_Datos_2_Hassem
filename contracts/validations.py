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
            print(messages['success']['contract'])
            return func(*args, **kwargs)
        else:
            print(messages['error']['contract'])
            return False
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
            print("Can't find the id")
            return False
    return check_contract
