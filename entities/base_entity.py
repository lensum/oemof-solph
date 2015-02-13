from oemof.helper import Timeseries


class Entity(object):

    def __init__(self, entity_id, position=None):
        self.id = entity_id
        self.position = position
        self.balance = Timeseries()