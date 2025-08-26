age=15
if age>=18:
    print("vous etes majeur")
elif age>=16:
    print("vous pouvez conduire")
else :
    print("vous etes mineur")
    
print("*"*245)    
    
nombre=float(input("entre un nombre"))
if nombre>0:
    print("le nombre est possitive")
elif nombre<0:
    print("le nombre est negative")
else :
    print("le nombre est nulle")

print("*"*245)

for i in range(21):
    i=i+1
    print(f"nombre {i}")
    
print("*"*245)    
    
mot=input("entre un nom")
for lettre in (mot):
    print(f"lettre {lettre}")
  
print("*"*245)  
    
for i in range(1,21,2):
    print(f"nombre {i}")

c=3
while c<5:
    print(f"copteur{c}")
    c=c+1
    
print("*"*245)
    
for i in range (10):
    if i==5:
        break
    print(i)
    
    
print("*"*245)
        
for i in range (10):
    if i%2==0:
        continue 
    print(i)

print("*"*245)

a=int(input("entres le multiblicateur"))
for i in range (1,13):
    r=a*i
    print(f"{a}*{i}={r}")
    