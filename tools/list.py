from quicksort import quicksort
from helpers.models import models
from classes.subject import Subject
from classes.subject_index import SubjectIndex
from tools.quicksort import quicksort

subject = Subject(_file=models['subject'])
subject_index = SubjectIndex(_file=models['subject_index'])

class Node(object):

  def __init__(self, *args, **kwargs):
    self.next_node = None
    self.prev_node = None
    self.value = kwargs



class DoublyList(object):

  def __init__(self, *args, **kwargs):
    self.anchor = None
    self.current = None
    self.count = 0
  
  def clear(self):
    self.anchor = None

  def show_all(self):

    aux = self.anchor
    while aux != None:
      if aux.value['status'] == 'True':
        print(aux.value)
      aux = aux.next_node

  def show_all_inv(self):

    aux = self.anchor
    ids = []
    while aux != None:
      if aux.value['status'] == 'True':
        print(aux.value)
        ids.append(int(aux.value['id']))
      aux = aux.next_node
    ids = quicksort(ids)
    for x in ids:
      print(self.search_one(str(x)))

  def add_one(self, **value):
    self.count += 1
    node = Node(**value)
    if self.anchor == None:
      self.anchor = node
      self.current = node
    else:
      self.current.next_node = node
      node.prev_node = self.current
      self.current = node

  def search_one(self, value):
    aux = self.anchor
    while aux != None:
      if aux.value['id'] == str(value) and aux.value['status'] == 'True':
        return aux.value
      aux = aux.next_node
    return None

  def update_one(self, value):
    aux = self.anchor
    while aux != None:
      if aux.value['id'] == str(value):
        print(aux.value)
        aux.value['name'] = raw_input("Escribe el nombre: ")
        aux.value['credits'] = raw_input("Escribe los creditos: ")
        aux.value['status'] = raw_input("Escribe el status (True | False): ")
        print(aux.value)
        return aux
      aux = aux.next_node
    return 'No encontrado'

  def delete_one_fisic(self, value):
    aux = self.anchor
    while aux != None:
      if aux.value['id'] == str(value) and aux.value['status'] == 'True':
        aux.prev_node.next_node = aux.next_node
        aux.next_node.prev_node = aux.prev_node
      aux = aux.next_node
    return None
  
  def delete_one_logic(self, value):
    aux = self.anchor
    while aux != None:
      if aux.value['id'] == str(value) and aux.value['status'] == 'True':
        print(aux.value)
        aux.value['status'] = 'False'
        print(aux.value)
        return aux
      aux = aux.next_node
    return 'No encontrado'
  
  def save_all(self):
    aux = self.anchor
    with open(models['subject'], 'w+') as file:
      file.write("")
    with open(models['subject_index'], 'w+') as file:
      file.write("")
    while aux != None:
      aux.value['type'] = 'subject'
      subject_index_obj = {
        'direction': aux.value['id'],
        'type': 'subject_index',
        'status': aux.value['status']
      }
      del aux.value['id']
      subject.create(**aux.value)
      subject_index.create(**subject_index_obj)
      aux = aux.next_node
