from crud.dimensionfields import CRUD


class Rol(CRUD):

    def __init__(self, *args, **kwargs):
      super(Rol, self).__init__(*args, **kwargs)
      self.type = 'Rol'
