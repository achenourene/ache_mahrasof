class Voiture:
    def __init__(self,marque,couleur):
        self.marque = marque
        self.couleur = couleur
        self.moteur_allume = False
    def demarrer(self):
        if not self.moteur_allume:
            self.moteur_allume=True
            print(F"la {self.marque} demarre.... vroom!")
        else:
            print("la voiture est deja demarrer")
v1=Voiture("toyota","rouge")
v1.demarrer()