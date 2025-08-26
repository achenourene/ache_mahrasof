class Personne:
    def __init__(self,nom,age):
        self.nom = nom
        self.age = age
    def se_presenter(self):
        print(F"bonjour,je suis {self.nom} est j'ai {self.age} ans")
ache=Personne("ache",25)
tombo=Personne("tombo",19)

ache.se_presenter()
tombo.se_presenter()
    