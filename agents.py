class Agent:

    def __init__(self, id):
        self.id = id


class Acheteur(Agent):

    def __init__(self, id, prixMax):
        Agent.__init__(self, id)
        self.prixMax = prixMax


class Vendeur(Agent):

    def __init__(self, id, prixMin):
        Agent.__init__(self, id)
        self.prixMin = prixMin

    
