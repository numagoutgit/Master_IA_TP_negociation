import numpy as np

from offre import *
from agents import *
from item import *

class Negociation:
    """Class où se déroule la négociation entre Vendeurs et Acheteurs pour un item donné.
       Attributs:
       - item : item de la négociation
       - acheteurs = liste des agents acheteurs
       - vendeurs = liste des agents vendeurs
       - duree = duree de la négociation
       - offres : Liste de taille durée, répertoriant toutes les offres ayant été faite lors d'un tour."""

    def __init__(self, item, nb_acheteurs, nb_vendeurs, duree):
        self.item = item
        self.duree = duree
        self.acheteurs = [Acheteur(i, nb_vendeurs, np.random.randint(120,150)) for i in range(nb_acheteurs)]
        self.vendeurs = [Vendeur(i, nb_acheteurs, np.random.randint(120,150)) for i in range(nb_acheteurs)]
        self.offres = [[] for i in range(duree)]