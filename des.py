import random
compteur=[0,0,0,0,0,0]
for i in range(100):
    de =random.randint(1,6)
    compteur.append(de)
for i in range(1,7):
    print(f"le nombre de {i} repete est : {compteur.count(i)}")