with open("ache.txt",encoding="utf-8" ) as f:
   contenus=f.read()
   print(contenus)
    
with open("ache.txt",encoding="utf-8" ) as f:
   contenu_complet=f.read()
   print(contenu_complet)
    
    
with open("ache.txt",encoding="utf-8" ) as f:
   premier_ligne=f.readline()
   dexieme_ligne=f.readline()
   print(premier_ligne)
   print(dexieme_ligne)
    
    
with open("ache.txt", encoding="utf-8") as f:
   lignes=f.readlines()
   for ligne in lignes:
      print(ligne.strip())

