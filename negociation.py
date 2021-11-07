import numpy as np

from agents import *
from  item import *
from  offre import *

class Negociation:

    def __init__(self, item, duree, nbAcheteurs, nbVendeurs):
        self.item = item
        self.acheteurs = [Acheteur(i, nbVendeurs, np.random.randint(70,130), np.random.randint(0,duree)) for i in range(nbAcheteurs)]
        self.vendeurs = [Vendeur(i+nbAcheteurs, nbAcheteurs, np.random.randint(70,130), np.random.randint(0,duree)) for i in range(nbVendeurs)]
        self.duree = duree

        self.offres = [[] for i in range(duree)]

    def initialiserVentes(self):
        for i in range(len(self.vendeurs)):
            for j in range(len(self.acheteurs)):
                offre = self.vendeurs[i].faireOffreBase(self.item, self.acheteurs[j])
                self.offres[0].append(offre)
                self.vendeurs[i].offresConcurrents[j] = offre
                self.acheteurs[j].offresConcurrents[i] = offre

    def tour(self, i):
        for a in self.acheteurs:
            if a.deal == None:
                newOffres = a.tour(i)
                self.offres[i]+=newOffres
        for v in self.vendeurs:
            newOffres = v.tour(i)
            self.offres[i]+=newOffres


    def run(self):
        self.initialiserVentes()
        for i in range(self.duree):
            self.tour(i)

item = Item(1)
jeu = Negociation(item, 20, 10, 5)
jeu.run()
print([len(j) for j in jeu.offres])
print([len(j.deals) for j in jeu.vendeurs])