#import os 
#chemin_absolu= os.path.exists("donner_personnelle.txt")
#print(chemin_absolu)

#nom,extension=os.path. splitext("donner_personnelle.txt")
#print(f"nom:{nom}")
#print(f"Extension:{extension}")
from pathlib import Path

chemin=Path("exo1.py")
print(f"le nom du fichier :{chemin.name}")
print(f"l'existance du fichier:{chemin.suffix}")
print(f"repertoire parent:{chemin.parent}")
print(f"chemin absolu:{chemin.absolute()}")
print(f"le chemin existe:{chemin.exists()}")
print(f"est un fichier:{chemin.is_file()}")
print(f"est un dossier :{chemin.is_dir()}")


dossier=Path("achenourene")
dossier.mkdir(exist_ok=True)

dossier=Path("achenourene/programme/exo/exo1.py")
dossier.mkdir(parents=True ,exist_ok=True)
print(f"le nom du fichier :{ dossier.name}")
print(f"l'existance du fichier:{ dossier.suffix}")
print(f"repertoire parent:{ dossier.parent}")
print(f"chemin absolu:{ dossier.absolute()}")
print(f"le chemin existe:{ dossier.exists()}")
print(f"est un fichier:{ dossier.is_file()}")
print(f"est un dossier :{dossier.is_dir()}")
