import json

def lire_json(nouveau_fichier):
    try:
        with open(nouveau_fichier,"r") as fichier:
            donnees=json.load(fichier)
            return donnees
    except json.JSONDecodeError:
        print("Erreur:fichier json introvable")
        return None
    
    

lecture=lire_json("sample.json")
print(lecture)

renseignement={
    "name": "John",
    "age": 25,
    "ville":"N'Djamena",
    "hobbies": ["reading", "traveling", "programming"]
  }

def ecrire_json(nouveau_fichier,renseignement):
    with open(nouveau_fichier,"w") as fichier:
        json.dump(renseignement,fichier,indent=4)
        
        
        
ecrire_json("personnelle.json",renseignement)
 