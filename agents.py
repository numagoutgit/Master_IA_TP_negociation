import numpy as np

from offre import *
from item import *

class Agent:

    def __init__(self, agentId, nbConcurrent):
        self.agentId = agentId
        self.offresConcurrents = [None for i in range(nbConcurrent)]

    def tour(self, i):
        res = []
        achat = False
        for o in self.offresConcurrents:
            if o.status == None:
                analyse = self.etudeProposition(o, i)
                o.etudeOffre(analyse)
            if o.status == "accepter":
                if o.date < i+5:
                    self.conclureDeal(o)
                    if isinstance(self, Acheteur):
                        achat = True
                        break
            elif o.status == "negocier":
                if self == o.faiseur:
                    newOffre = self.faireOffre(o.item, np.random.randint(70,130), i, o.receveur)
                else:
                    newOffre = self.faireOffre(o.item, np.random.randint(70,130), i, o.faiseur)
                res.append(newOffre)
            else:
                if o.date < i+5:
                    if self == o.faiseur:
                        newOffre=self.faireOffre(o.item, np.random.randint(70,130),i,o.receveur)
                    else:
                        newOffre = self.faireOffre(o.item, np.random.randint(70,130), i, o.faiseur)
                    res.append(newOffre)
        if achat:
            return []
        else:
            return res
        
    def faireOffre(self, item, prix, date, receveur):
        offre = Offre(item, prix, date, self, receveur)
        if isinstance(receveur, Vendeur):
            self.offresConcurrents[receveur.agentId-len(receveur.offresConcurrents)] = offre
        else:
            self.offresConcurrents[receveur.agentId] = offre
        return offre


class Acheteur(Agent):

    def __init__(self, agentId, nbConcurrent, prixMax, dateLimiteMin):
        Agent.__init__(self, agentId, nbConcurrent)
        self.prixMax = prixMax
        self.dateLimiteMin = dateLimiteMin

        self.deal = None

    def etudeProposition(self, offre, n):
        if (offre.prix < self.prixMax*0.8 and offre.date > self.dateLimiteMin*1.2) or (n > 19 & offre.prix < self.prixMax and offre.date > self.dateLimiteMin):
            return "accepter"
        elif (offre.prix < self.prixMax and offre.date > self.dateLimiteMin):
            return "negocier"
        else:
            return "refuser"

    def conclureDeal(self, offre):
        self.deal = offre



class Vendeur(Agent):

    def __init__(self, agentId, nbConcurrent, prixMin, dateLimiteMax):
        Agent.__init__(self, agentId, nbConcurrent)
        self.prixMin = prixMin
        self.dateLimiteMax = dateLimiteMax

        self.deals = []

    def faireOffreBase(self, item, receveur):
        return Offre(item, 2*self.prixMin, 1/2*self.dateLimiteMax, self, receveur)

    def etudeProposition(self, offre, n):
        if (offre.prix > self.prixMin*1.2 and offre.date < self.dateLimiteMax*0.8) or (n > 19 & offre.prix > self.prixMin and offre.date < self.dateLimiteMax):
            return "accepter"
        elif (offre.prix > self.prixMin and offre.date < self.dateLimiteMax):
            return "negocier"
        else:
            return "refuser"

    def conclureDeal(self, offre):
        self.deals.append(offre)