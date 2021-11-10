import numpy as np

from negociation import *

item = Item(0, 200)

#Test d'execution
jeu = Negociation(item,5,5,5,2,2,2)
jeu.run()
print([v.argent_gagne() for v in jeu.vendeurs])