import numpy as np

from agents import *
from item import *

class Offre:
    """Class représentant une offre d'un agent à un autre pour un service donné.
       Attributs:
       - item : service associé à l'offre
       - prix : prix proposé pour le service
       - date : date de l'offre
       - faiseur : agent faisant l'offre
       - receveur : agent recevant l'offre"""
    def __init__(self, item, prix, date, faiseur, receveur):
        self.item = item
        self.prix = prix
        self.date = date
        self.faiseur = faiseur
        self.receveur = receveur