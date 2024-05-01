from joueur import Joueur

class Equipe:
    def __init__(self):
        self.membres = []

    def ajouter_membre(self, joueur):
        self.membres.append(joueur)

    def supprimer_membre(self, joueur):
        self.membres.remove(joueur)