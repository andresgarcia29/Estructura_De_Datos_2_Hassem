from crud.fixposition import CRUD


class Offer(CRUD):

    def __init__(self, *args, **kwargs):
      super(Offer, self).__init__(*args, **kwargs)
      self.type = 'offer'

    def get_group_by_periods(self, id_period):
      offers = self.get_all(False)

      current = []
      for offer in offers:
        print(offer)
        if str(offer['period']) == str(id_period):
          current.append(offer)
      return current
