from crud.dimensionfields import CRUD


class User(CRUD):

    def __init__(self, *args, **kwargs):
      super(User, self).__init__(*args, **kwargs)
      self.type = 'user'
