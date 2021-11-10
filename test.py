import numpy as np

from negociation import *

item = Item(0, 200)

#Test d'execution
for k in range(100):
    jeu = Negociation(item,5,5,5,2,2,2)
    jeu.run()