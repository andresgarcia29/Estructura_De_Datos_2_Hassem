from crud.delimiters import CRUD

class Teacher(CRUD):

    def __init__(self, *args, **kwargs):
      super(Teacher, self).__init__(*args, **kwargs)
      self.type = 'teacher'