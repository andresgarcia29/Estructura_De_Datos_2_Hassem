print("Create user")
from helpers.order import sort_like_contracts, sort_update_like_contracts, sort_register_to_object

def createUser():
  dicionary = {
    "id": "22",
    "name": "Andres",
    "cellphone": "839084093",
    "email": "jose.andres.gm29@gmail.com",
    "type": "teacher"
  }
  sort = sort_like_contracts(**dicionary)
  string = ""
  for x in sort:
    lenght_string = len(x)
    len_id = len(str(lenght_string))
    string += str(len_id) + str(lenght_string) + x
  return (string)

def readObject(string):
  object = []
  def one_by_one(size, position):
    current_value = int(string[size])
    position+=1
    all_size = string[position : current_value + position]
    position+=current_value
    value = string[position:position+int(all_size)]
    position+=int(all_size)
    object.append(value)
    if position != len(string):one_by_one(position, position)
  one_by_one(0, 0)
  string = "".join([x + '|' for x in object])[0:-1]
  print(string)
  dct = {
      'type': 'teacher',
      'register': string
  }
  print(sort_register_to_object(**dct))


readObject('110214hola@gmail.com17hola123')
