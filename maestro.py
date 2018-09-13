from classes.subject import Subject
from classes.subject_index import SubjectIndex
from tools.list import DoublyList
from helpers.models import models
import threading
import time

dlist = DoublyList()

subject = Subject(_file=models['subject'])
subject_index = SubjectIndex(_file=models['subject_index'])

def getAll():
  dlist.clear()
  registers = subject_index.get_all(True)
  if len(subject_index.get_all(True)) > 0:
      for i, x in enumerate(registers):
        dlist.add_one(**subject.get_one(x['id'], **{'delet_fisic': True}))

getAll()


def save():
  while True:
    time.sleep(10)
    print("Lista guardada correctamente")
    dlist.save_all()
    getAll()

def menu():
  while True:

      print("1: Crear Asignatura")
      print("2: Ver todas las asignaturas")
      print("3: Buscar Asignatura (id)")
      print("4: Actualizar Asignatura")
      print("5: Ver Asignaturas ordenadas (-1)")
      print("6: Borrar Asignatura Logicamente")
      print("7: Borrar Asignatura Fisicamente")
      print("8: Guardar Todo")
      print("9: Salir")
      option = int(input("Que deseas hacer?: "))

      if option == 1:
        name = raw_input("Escribe el nombre: ")
        credits_input = raw_input("Escribe los creditos: ")
        new_record = {
            'id': str(dlist.count + 1),
            'name': name,
            'credits': credits_input,
            'status': 'True'
        }
        dlist.add_one(**new_record)
        print("Asignatura creada correctamente")

      elif option == 2:
        dlist.show_all()

      elif option == 3:
        print(dlist.search_one(input("Escribe el id: ")))

      elif option == 4:
        dlist.update_one(input("Escribe el id: "))

      elif option == 5:
        dlist.show_all_inv()
      
      elif option == 6:
        dlist.delete_one_logic(input("Escribe el id: "))
      
      elif option == 7:
        dlist.delete_one_fisic(input("Escribe el id: "))

      elif option == 8:
        dlist.save_all()
        getAll()

      elif option == 9:
        break

      else:
        print("Opciion invalida")

t1 = threading.Thread(target=menu)
t2 = threading.Thread(target=save)

t1.start()
t2.start()

t1.join()
t2.join()
