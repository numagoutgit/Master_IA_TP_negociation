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

    def __init__(self, item, nb_acheteurs_random, nb_acheteurs_moite, nb_acheteurs_borne, nb_vendeurs_random, nb_vendeurs_moitie, nb_vendeurs_borne, duree):
        self.item = item
        self.duree = duree
        nb_acheteurs = nb_acheteurs_borne+nb_acheteurs_moite+nb_acheteurs_random
        nb_vendeurs = nb_vendeurs_borne+nb_vendeurs_moitie+nb_vendeurs_random
        self.acheteurs = []
        self.vendeurs = []
        for k in range(nb_acheteurs):
            if k < nb_acheteurs_borne:
                self.acheteurs.append(Acheteur_borne(k,nb_vendeurs,np.random.randint(120,150)))
            elif k < nb_acheteurs_borne+nb_acheteurs_moite:
                self.acheteurs.append(Acheteur_moitie(k,nb_vendeurs,np.random.randint(120,150)))
            else:
                self.acheteurs.append(Acheteur_random(k,nb_vendeurs,np.random.randint(120,150)))
        for k in range(nb_vendeurs):
            if k < nb_vendeurs_borne:
                self.vendeurs.append(Vendeur_borne(k, nb_acheteurs, np.random.randint(120,150)))
            elif k < nb_vendeurs_borne+nb_vendeurs_moitie:
                self.vendeurs.append(Vendeur_moitie(k, nb_acheteurs, np.random.randint(120,150)))
            else:
                self.vendeurs.append(Vendeur_random(k, nb_acheteurs, np.random.randint(120,150)))

        self.offres = [[] for i in range(duree)]

    def initialiser_offres(self):
        """Initialise les offres en commençant par les vendeurs qui font une offre à tout le monde"""
        for vendeur in self.vendeurs:
            prix = np.random.randint(vendeur.prix_min, vendeur.prix_min*2)
            for acheteur in self.acheteurs:
                offre = vendeur.proposer_offre(self.item, prix, acheteur, 0)
                self.offres[0].append(offre)

    def effecuer_tour(self, i):
        """Effectue le tour i du jeu, les acheteurs commencent puis les vendeurs suivent"""
        for acheteur in self.acheteurs:
            if acheteur.deal == None:
                offres = acheteur.tour(i)
                self.offres[i] += offres
        for vendeur in self.vendeurs:
            offres = vendeur.tour(i)
            self.offres[i] += offres

    def run(self):
        """Execute l'algorithme de jeu complet"""
        self.initialiser_offres()
        for k in range(1, self.duree):
            self.effecuer_tour(k)
