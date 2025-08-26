mes_personne=["1 safia \n2 makka \n3 mariame \n4 sadie \n5 kaltoma"]
with open("donner_personnelle.txt","w") as f:
     f.writelines(mes_personne)
     
with open("donner_personnelle.txt","a") as f:
     f.write("\n6 ache")
    