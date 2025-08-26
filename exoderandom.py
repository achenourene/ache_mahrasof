import random
print(random.random())
print(random.randint(1,10))


couleur=['rouge','vert','bleu','jaune']
print(random.choice(couleur))

nombre=[1,2,3,4,5]
random.shuffle(nombre)
print(nombre)
print(random.sample(couleur,2))
print(len(nombre))

compteur=[0,0,0,0,0,0]
for i in range(100):
    de =random.randint(1,6):
        compteur=compteur+1
        
        
jeu=['pierre','papier']
