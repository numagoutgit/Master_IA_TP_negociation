import numpy as np

from offre import *

class Agent:
    """Super-class agent. Correspond aux Vendeurs/Acheteurs qui se feront des offres à propos d'un item.
       Attribute:
        - agentId
        - offre_concurrents : Liste de la dernière offre entre l'agent et le concurrents situé à la ie place de la liste"""
    def __init__(self, agentId, nb_adversaires):
        self.agentId = agentId
        self.offre_concurrents = [None for i in range(nb_adversaires)]

    def etude_offre(self, offre):
        """Renvoie un string indiquant si l'agent accepter l'offre, refuse ou choisis de négocier"""    
        if isinstance(self, Acheteur):
            if offre.prix > 1.2 * self.prix_max:
                return "refuser"
            elif offre.prix < 0.8 * self.prix_max:
                return "accepter"
            else:
                return "negocier"
        else:
            if offre.prix < 0.8 * self.prix_min:
                return "refuser"
            elif offre.prix > 1.2 * self.prix_min:
                return "accepter"
            else:
                return "negocier"     

    def conclure_deal(self, offre):
        """Conclut le deal, si l'agent est un acheteur alors il ne peut plus acheter, si c'est un vendeur il peut encore négocier avec les acheteurs n'ayant pas encore conclut"""
        if isinstance(self, Acheteur):
            self.deal = offre
            for o in self.offre_concurrents:
                o.set_status('annuler')
        else:
            self.deals.append(offre)

    def proposer_offre(self, item, prix, agent, date):
        """Propose une offre concernant l'item à un agent"""
        offre = Offre(item, prix, date, self, agent)
        self.offre_concurrents[agent.agentId] = offre
        agent.offre_concurrents[self.agentId] = offre
        return offre

    def meilleure_offre(self, offres):
        """Renvoie la meilleure offre parmi une liste d'offre"""
        prix = [offre.prix for offre in offres]
        if isinstance(self, Acheteur):
            return offres[prix.index(min(prix))]
        return offres[prix.index(max(prix))]

    def tour(self, i):
        """L'agent joue son tour. Il étudie toutes les offres auxquelles il est affilié, puis il négocie à qui il juge nécessaire. Enfin il vérifie si une de ces offres n'a pas été accepté, si oui il choisi la meilleure"""
        offre_acceptee = []
        offre_negocier = []
        offres = []
        for offre in self.offre_concurrents:
            if offre.status == None:
                etude = self.etude_offre(offre)
                offre.set_status(etude)
            if offre.status == 'negocier':
                offre_negocier.append(offre)
            elif offre.status == 'accepter':
                offre_acceptee.append(offre)
        if len(offre_acceptee) != 0:
            if isinstance(self, Acheteur):
                best_offre = self.meilleure_offre(offre_acceptee)
                self.conclure_deal(best_offre)
            else:
                for o in offre_acceptee:
                    self.conclure_deal(o)
        for offre in offre_negocier:
            if isinstance(self, Acheteur):
                if len(offre_acceptee) == 0:
                    prix = self.proposer_prix(offre)
                    offres.append(self.proposer_offre(offre.item, prix, offre.faiseur, i))
                else:
                    offre.set_status("annuler")
            else:
                prix = self.proposer_prix(offre)
                offres.append(self.proposer_offre(offre.item, prix, offre.faiseur, i))
        return offres

          
class Acheteur(Agent):
    """Correspond à l'acheteur du service. Son but est de payer son service le moins cher possible.
       Attributs:
       - agentId
       - offre_concurrents
       - prix_max : Prix maximum que l'Acheteur est prêt à payer
       - deal : Offre que l'acheteur a conclu"""

    def __init__(self, agentId, nb_adversaires, prix_max):
        Agent.__init__(self, agentId, nb_adversaires)
        self.prix_max = prix_max
        self.deal = None

class Vendeur(Agent):
    """Correspond au vendeur du service. Son but est de vendre ses services aux acheteurs et de gagner le plus d'argent possible.
       Attributs:
       - agentId
       - offre_concurrents
       - prix_min : Prix minimum que le vendeur est prêt à vendre
       - deals : Liste des offres que le vendeur a conclus"""

    def __init__(self, agentId, nb_adversaires, prix_min):
        Agent.__init__(self, agentId, nb_adversaires)
        self.prix_min = prix_min

        self.deals = []

class Acheteur_random(Acheteur):
    """Acheteur avec le comportement random"""
    def __init__(self, agentId, nb_adversaires, prix_max):
        Acheteur.__init__(self, agentId, nb_adversaires, prix_max)

    def proposer_prix(self, offre):
        """Propose un prix"""
        prix = np.random.randint(self.prix_max//2, self.prix_max)
        return prix

class Vendeur_random(Vendeur):
    """Vendeur avec le comportement random"""
    def __init__(self, agentId, nb_adversaires, prix_min):
        Vendeur.__init__(self, agentId, nb_adversaires, prix_min)

    def proposer_prix(self, offre):
        """Prospose un prix"""
        prix = np.random.randint(self.prix_min, self.prix_min*2)
        return prix