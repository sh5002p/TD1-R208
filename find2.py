import os
import sys

listeFichier = []
listeDossiers = []

def recherche(d):
    global listeFichier
    global listeDossiers
    for elt in os.listdir(d):
        if os.path.isfile(d+"\\"+elt):
            listeFichier.append(d+"\\"+elt)
        elif os.path.isdir(d+"\\"+elt):
            listeDossiers.append(d+"\\"+elt)


def affiche():
    """

    :param d:
    :return:
    """
    for elt in listeDossiers:
        print(elt)
    for elt1 in listeFichier:
        print(elt1)


if __name__ == '__main__':
    recherche(sys.argv[1])
    if len(listeDossiers) > 0:
        for e in listeDossiers:
            recherche(e)
    affiche()