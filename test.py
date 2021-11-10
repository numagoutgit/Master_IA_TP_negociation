import numpy as np

from negociation import *

item = Item(0)

#Test d'execution
for k in range(1000):
    jeu = Negociation(item,5,5,5,2,2,2,20)
    jeu.run()