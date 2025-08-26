class CompteBancaire:
    def __init__(self,titulaire,solde_initial=0):
        self.titulaire=titulaire
        self.solde=solde_initial
        self.historique=[]
    
    
    def deposer(self,montant):
        if montant > 0:
            self.solde += montant
            self.historique.append(F"Depot: +{montant} fcfa")
            print(F"Depot de {montant} fcfa effectue. Nouveau solde:{self.solde} fcfa")
        else:
            print("le montant doit etre positif")
    def retirer(self,montant):
        if montant > 0:
            if self.solde >= montant:
                self.solde -= montant
                self.historique.append(F"retrait: -{montant} fcfa")
                print(F"retrait de {montant} fcfa effectue. Nouveau solde:{self.solde} fcfa")
            else:
                print("solde insuffisant")
        else:
            print("le montant doit etre positif")
    def consulter_solde(self):
        print(F"solde du compte de {self.titulaire} : {self.solde} fcfa")
        
    def afficher_historique(self):
        print(f"Historiquedu compte de {self.titulaire} :")
        for operation in  self.historique:
            print(F"-{operation}")
            
            
compte_ache = CompteBancaire("ache",50000)
compte_ache.deposer(100000)
compte_ache.retirer(2000)
compte_ache.consulter_solde()
compte_ache.afficher_historique()

                
            
    
