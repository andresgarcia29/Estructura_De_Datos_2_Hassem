"""
  Teacher's: This file container all the logic to create a CRUD of Teachers.
"""

from controller.teacher import Teacher

obj = {
  'type': 'teacher',
  'name': 'Pedro',
  'email': 'andres@gmail.com',
  'cellphone': '3393939',
}

file = {
  '_file': 'files/Teachers.txt',
}

obj_update = {
    'type': 'teacher',
    'id': '4',
    'name': 'Ricardo Arjona',
    'email': 'perro@delmal.com',
}

crd = Teacher(**file)
# print(crd.get_one_by_id(30))
# crd.delete(int(input("DeletE: ")))
crd.update(**obj_update)
# for x in range(0,20):
#   crd.create(**obj)
