import os
import sys

listeFichier = []
listeDossiers = []

def recherche(d,f):
    global listeFichier
    global listeDossiers
    for elt in os.listdir(d):
        if os.path.isfile(d+"\\"+elt):
            if elt == f:
                listeFichier.append(d+"\\"+elt)
        elif os.path.isdir(d+"\\"+elt):
            listeDossiers.append(d+"\\"+elt)


def affiche():
    """

    :param d:
    :return:
    """
    for elt in listeFichier:
        print(elt)


if __name__ == '__main__':
    recherche(sys.argv[1], sys.argv[2])
    if len(listeDossiers) > 0:
        for e in listeDossiers:
            recherche(e,sys.argv[2])
    affiche()