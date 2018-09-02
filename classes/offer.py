from crud.fixposition import CRUD


class Offer(CRUD):

    def __init__(self, *args, **kwargs):
      super(Offer, self).__init__(*args, **kwargs)
      self.type = 'offer'
