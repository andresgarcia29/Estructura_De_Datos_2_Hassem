from contracts.fields import contracts
from helpers.constant import delimiter

def sort_like_contracts(**kwargs):
    order = contracts[kwargs['type']]
    del kwargs['type']
    object_sort = []
    for x in order:
      object_sort.append(kwargs[x])
    object_sort.insert(0, kwargs['id'])
    return object_sort

def sort_update_like_contracts(**kwargs):
    #Get the order of object
    order = contracts[kwargs['obj']['type']]
    if order[0] != 'id':
        order.insert(0, 'id')

    #Delete the type of fild
    del kwargs['obj']['type']

    #Convert to a array and delete the break lines
    register = kwargs['register'].split(delimiter)
    register = [x.replace('\n', '') for x in register]

    #Make a dictionary with the registers
    dictionary = {}
    for i, x in enumerate(register):
        dictionary[order[i]] = register[i]

    #Get the items that have to change
    items_to_update = kwargs['obj'].keys()
    for x in items_to_update:
        dictionary[x] = kwargs['obj'][x]

    #Give and order to the dicionary and convert to array
    items = []
    for x in order:
      items.append(dictionary[x])

    return items

def sort_register_to_object(**kwargs):
    #Get the order of object
    order = contracts[kwargs['type']]
    if order[0] != 'id':
        order.insert(0, 'id')

    #Delete the type of fild
    del kwargs['type']

    #Convert to a array and delete the break lines
    register = kwargs['register'].split(delimiter)
    register = [x.replace('\n', '') for x in register]

    #Make a dictionary with the registers
    dictionary = {}
    for i in range(0, len(register)):
        dictionary[order[i]] = register[i]

    return dictionary
