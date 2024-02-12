import sys
import os


def start_find2(directory):
    listeFichiers = []
    listeDossiers = []

    def recherche(directory):


        for nom in os.listdir(directory):
            chemin = os.path.join(directory, nom)

            if os.path.isfile(chemin):
                listeFichiers.append(chemin)
            elif os.path.isdir(chemin):
                listeDossiers.append(chemin)
                recherche(chemin)

    recherche(directory)

    return listeFichiers, listeDossiers


if __name__ == '__main__':
    directory = input("Entrez le nom du dossier à explorer : ")
    listeFichiers, listeDossiers = start_find2(directory)

    print("Fichiers :")
    for fichier in listeFichiers:
        print(fichier)

    print("\nDossiers :")
    for dossier in listeDossiers:
        print(dossier)