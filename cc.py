import csv
def lire_csv(clients_csv):
    with open(clients_csv,"r",  newline="") as f:
        lecteur=csv.reader(f)
        for ligne in lecteur:
            print(ligne)
lire_csv("clients.csv")

def lire_csv_dict(clients_csv):
    with open(clients_csv,"r",  newline="\n") as f:
        lecteur=csv.DictReader(f)
        for ligne in lecteur:
            print(ligne)
resultat=lire_csv_dict("clients.csv")
 