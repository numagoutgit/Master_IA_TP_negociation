import numpy as np

class Item:
    """Classe correspondant à un service/item.
       Attribute:
         - itemId"""
    def __init__(self, itemId, date_max):
        self.itemId = itemId
        self.date_max = date_max