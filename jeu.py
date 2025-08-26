import random
listes_jeux=['pierre','papier','ciseaux']
jeu=random.choice(listes_jeux)
choix=input("entres votre choix")
if choix=="pierre" and jeu=="papier":
    print("l'ordinateur a gagne")
elif choix=="pierre" and jeu=="ciseaux":
    print("je gagne")
elif choix=="ciseaux" and jeu=="papier":
    print("je gagne")
elif choix=="ciseaux" and jeu=="pierre":
    print("l'ordinateur a gagne")
elif choix=="papier" and jeu=="pierre":
    print("je gagne")
elif choix=="papier" and jeu=="ciseaux":
    print("l'ordinateur a gagne")

elif choix==jeu:
    print("Ache et l'ordinateur ont eu un match nul")
else:
    print("un erreur c'est produit")
