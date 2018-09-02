from crud.fixposition import CRUD


class Group(CRUD):

    def __init__(self, *args, **kwargs):
      super(Group, self).__init__(*args, **kwargs)
      self.type = 'group'
