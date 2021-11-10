import numpy as np
import matplotlib.pyplot as plt

from negociation import *

def main(nbA_rand, nbA_m, nbA_bor, nbV_rand, nbV_m, nbV_bor, n, d):
    v_born = []
    v_rand = []
    v_moit = []

    a_born = []
    a_rand = []
    a_moit = []

    item = Item(0,d)
    for k in range(n):
        jeu = Negociation(item, nbA_bor, nbA_m, nbA_rand, nbV_rand, nbV_m, nbV_bor)
        jeu.run()
        for a in jeu.acheteurs:
            if isinstance(a, Acheteur_borne):
                a_born.append(a.argent_paye())
            elif isinstance(a, Acheteur_moitie):
                a_moit.append(a.argent_paye())
            elif isinstance(a, Acheteur_random):
                a_rand.append(a.argent_paye())

        for v in jeu.vendeurs:
            if isinstance(v, Vendeur_borne):
                v_born.append(v.argent_gagne())
            elif isinstance(v, Vendeur_moitie):
                v_moit.append(v.argent_gagne())
            elif isinstance(v, Vendeur_random):
                v_rand.append(v.argent_gagne())

    v_born = np.array(v_born)
    v_moit = np.array(v_moit)
    v_rand = np.array(v_rand)

    a_born = np.array(a_born)
    a_rand = np.array(a_rand)
    a_moit = np.array(a_moit)

    a_born, nan_born = a_born[~np.isnan(a_born)], np.sum(np.isnan(a_born))
    a_rand, nan_rand = a_rand[~np.isnan(a_rand)], np.sum(np.isnan(a_rand))
    a_moit, nan_moit = a_moit[~np.isnan(a_moit)], np.sum(np.isnan(a_moit))

    Y = [np.mean(v_born), np.mean(v_moit), np.mean(v_rand), np.mean(a_born), np.mean(a_moit), np.mean(a_rand)]
    X = ['Vendeur borné', 'Vendeur moitié', 'Vendeur aléatoire', 'Acheteur borné', 'Acheteur moitié', 'Acheteur aléatoire']

    fig, ax = plt.subplots(figsize=(200,200))
    bar = ax.bar(X,Y, width = 0.35)
    ax.bar_label(bar, label_type='edge', labels = ['sigma = {:.2f}'.format(np.std(v_born)), 'sigma = {:.2f}'.format(np.std(v_rand)), 'sigma = {:.2f}'.format(np.std(v_moit)), 'nb_nan = {:.2f}'.format(nan_born/n), 'nb_nan = {:.2f}'.format(nan_rand/n), 'nb_nan = {:.2f}'.format(nan_moit/n)])
    plt.show()

if __name__ == "__main__":
    main(10,10,10,5,5,5,100,30)