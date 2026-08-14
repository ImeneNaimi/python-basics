import math 
num=int(input("Enter a number: "))
print("The square root of this number is: ")
print(math.sqrt(num))

dec=float(input("Enter a decimal number: "))
print(math.floor(dec))
print(math.ceil(dec))

print("La valeur de pi= ",math.pi)
ray=int(input("Entrer le rayon d'un cercle: "))
Aire=math.pi * ray**2
print(Aire)


import random
print(random.randint(1,100))

movies = ["Inception", "Interstellar", "The Matrix", "Dune"]
print(random.choice(movies))

number=random.randint(1,20)
n=int(input("Enter a number to guess: "))
while(n!=number):
 if n<number:
    print("Trop petit")
    n=int(input("Enter a number to guess: "))
 elif n>number:
    print("trop grand")
    n=int(input("Enter a number to guess: "))
print("Bravo!")
 

names=[]
for i in range(5):
    name=input("Enter a name: ")
    names.append(name)
print("The winner is: ")
print(random.choice(names))    

plen=int(input("password length: "))
password=""
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
for i in range(plen):
    password+=random.choice(characters)
print(password)    
                    
