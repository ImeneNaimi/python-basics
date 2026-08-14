try:
    num=int(input("Enter an integer: "))
except ValueError:
    print("Invalid number! ")

try:
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    print(a / b)
except ValueError:
    print("Invalid number! please enter an integer value ")
except ZeroDivisionError:
    print("Division by zero is impossible.")

try:  
    age=int(input("Enter your age please: "))
except ValueError:
    print("Invalid input.")
else:
    print("Next year you will be: ", age+1)
    
try: 
    with open("text.txt","r") as file:
        contenu=file.read()
        print(contenu)
except FileNotFoundError:
    print("File not found!")


numbers=[]
i=0
while i<5:
     try:
        numero=int(input("Enter a number: "))
        numbers.append(numero)
        i+=1
     except ValueError:
        print("Enter an integer value! ")
print(numbers)

    