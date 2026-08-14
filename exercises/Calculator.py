def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

a=int(input("Enter the first number please: "))
b=int(input("Enter the second number please: "))
op=input("Choose an operation: ")

if op=="+":
    print(add(a,b))
elif op=="-":
    print(subtract(a,b))  
elif op=="*":
    print(multiply(a,b))      
elif op=="/":
    if b == 0:
     print("Cannot divide by zero.")
    print(divide(a,b))
else:
    print("Invalid operation!")