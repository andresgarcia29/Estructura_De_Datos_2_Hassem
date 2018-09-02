from crud.fixposition import CRUD


class Period(CRUD):

    def __init__(self, *args, **kwargs):
      super(Period, self).__init__(*args, **kwargs)
      self.type = 'period'
