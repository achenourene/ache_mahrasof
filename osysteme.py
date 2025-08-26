import os

print(os.getcwd())




if os.path.exists("exo1.py"):
    print("le fichier existe")
else:
    print("aucun resultat existant")

nourene=os.path.join("C:", "Users", "nousr")
print(nourene)
fichiers=os.listdir("C:/Users/nousr")
print(fichiers)
if os.path.exists("programme3.py"):
    taille=os.path.getsize("programme3.py")
    print(f"Taille:{taille} bits")
    

os.mkdir("ache")
os.rmdir("./ache")
os.remove("nousradine.py")