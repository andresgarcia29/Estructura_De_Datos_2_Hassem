from crud.fixposition import CRUD


class Subject(CRUD):

    def __init__(self, *args, **kwargs):
      super(Subject, self).__init__(*args, **kwargs)
      self.type = 'subject'