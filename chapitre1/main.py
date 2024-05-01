import time
import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(os.path.abspath(os.path.join(dir_path, '..', 'mise_en_place')))

from joueur import Joueur
from scenario1 import Scenario1

def main():
    print("Bienvenue sur Ethereal")
    nom = input("Entrer votre nom: ")
    joueur = Joueur(nom)
    time.sleep(2)
    print("Votre aventure commence maintenant!")

    Scenario1(joueur) 

if __name__ == "__main__":
    main()
