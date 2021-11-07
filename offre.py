import numpy as np

from agents import *
from offre import *

class Offre:

    def __init__(self, item, prix, date, faiseur, receveur):
        self.item = item
        self.prix = prix
        self.date = date
        self.faiseur = faiseur
        self.receveur = receveur
        self.status = None

    def etudeOffre(self, status):
        self.status = status