from crud.fixposition import CRUD


class SubjectIndex(CRUD):

    def __init__(self, *args, **kwargs):
      super(SubjectIndex, self).__init__(*args, **kwargs)
      self.type = 'subject_index'
