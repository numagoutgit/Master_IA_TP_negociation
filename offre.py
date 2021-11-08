import numpy as np

from item import *

class Offre:
    """Class représentant une offre d'un agent à un autre pour un service donné.
       Attributs:
       - item : service associé à l'offre
       - prix : prix proposé pour le service
       - date : date de l'offre
       - faiseur : agent faisant l'offre
       - receveur : agent recevant l'offre
       - status : Status de l'offre ('accepter', 'negocier', 'refuser', 'annuler', None)
       - """
    def __init__(self, item, prix, date, faiseur, receveur):
        self.item = item
        self.prix = prix
        self.date = date
        self.faiseur = faiseur
        self.receveur = receveur

        self.status = None

    def __repr__(self):
        string = '(prix = {}, date = {}, faiseur = {}, receveur = {}, status = {})'.format(self.prix, self.date, self.faiseur.agentId, self.receveur.agentId, self.status)
        return string

    def set_status(self, status):
        """Set status"""
        self.status = status