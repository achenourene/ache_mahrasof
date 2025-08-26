a=round(1.26897,2)
print(a)

nom="ache"
nom.split(sep=",")
print(nom)

liste1=list(range(10))
print(liste1)




c=zip([1,2],["a","b"]) 
for r in c:
    print(r)
    
c=list(zip([1,2],["a","b"]))
print(c)

a=list(map(int,{"1","2","5","4"}))
print(a)
liste=[1,5,9,7,6]

print(dir(liste))

print("abc".replace("a","z"))


text="c'est ache avec toi"
r=text.split()
print(r)
print(" ".join(r))

listee=[4,8,9,5,2,4]
init=set(listee)
print(init)