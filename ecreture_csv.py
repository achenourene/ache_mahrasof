import csv
def ecrire_csv(fichier,donnees):
    with open(fichier,"w",  newline="") as f:
        ecrivain=csv.writer(f)
    
        for ligne in donnees:
            ecrivain.writerow(ligne)
donnees=[
    ["nom","age","ville"],
    ["ache",35,"paris"],
    ["sadie",17,"paris"],
    ["safia",22,"N'Djamena"],
    ["mariam",17,"N'Djamena"],
    ["Makka",17,"N'Djamena"]
]
ecrire_csv("personnes.csv",donnees)