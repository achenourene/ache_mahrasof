fruits=["pomme","banane","orage","datte"]
mixte=["python",3.14,True,42]

print(fruits)
print(fruits[0])
print(fruits[-1])
fruits[1]="mangue"
print(fruits)
print(fruits[3])
fruits[0]="avocat"
print(fruits)
fruits.append("kiwi")
fruits.insert(1,"figue")
print(fruits)
print(fruits[4])


nombres=[3,1,4,1,5,9,2,6,1,1]
print(max(nombres))
print(min(nombres))
print(len(nombres))
print(sum(nombres))
print(nombres.count(1))
nombres.sort()
print(nombres)
nombres.remove(1)
del nombres[0]
element=nombres.pop()
print(nombres)