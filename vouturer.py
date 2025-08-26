class Voiture:
    def __init__(self,marque,modele,couleur,kilometrage=0):
        self.marque = marque
        self.modele = modele
        self.couleur = couleur
        self.kilometrage = kilometrage
        self.moteur_allume = False
    def demarrer(self):
        if not self.moteur_allume:
            self.moteur_allume=True
            print(F"la {self.marque} {self.modele} demarre.... vroom!")
        else:
            print("la voiture est deja demarrer")
    def arreter(self):
        if  self.moteur_allume:
            self.moteur_allume = False
            print(F"la {self.marque} {self.modele} s'arrete.")
        else:
            print("la voiture est deja arretee")
    def rouler(self,distance):
        if self.moteur_allume:
            self.kilometrage += distance
            print(F"vous avez roule {distance} km." F" kilometrage total: {self.kilometrage}")
        else:
            print("Demarrez d'abord la voiture")
    def info(self):
        etat = "demarree" if self.moteur_allume  else "arretee"
        print(f"voiture: {self.marque} {self.modele}")
        print(F"couleur: {self.couleur}")
        print(F"kilometrage: {self.kilometrage} km")
        print(F"etat: {etat}")
        
        
ma_voiture = Voiture("toyota","corolla","bleu")
sa_voiture = Voiture("BMW","X5","jaune", 1500)


print("=== Ma voiture ===") 
sa_voiture.info()
sa_voiture.demarrer()
sa_voiture.arreter()
sa_voiture.demarrer()
sa_voiture.rouler(10)
sa_voiture.rouler(10)
sa_voiture.rouler(10)
sa_voiture.rouler(10)
sa_voiture.rouler(10)
sa_voiture.rouler(10)
sa_voiture.arreter()    
    
            
            