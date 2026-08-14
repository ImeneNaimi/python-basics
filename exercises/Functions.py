def greet():
     print("Welcome to python")

for i in range(5):
     greet()

def greet(name):
     print("Hello ",name)

greet("Imene")
greet("Amina")
greet("Souhila")

def rectangle_area(length,width):
     return length*width

l=int(input("Please enter the length of this rectangle: "))
w=int(input("Please enter the width of this rectangle: "))
area=rectangle_area(l,w)
print("The area of thise rectangle: ",area)

def largest(a,b):
    """ if a>b:
          return a
     else:
          return b"""
    return max(a,b)

big=largest(12,40)
print("The largest number between 12 and 40 is: ",big)   

def is_even(number):
     if number%2==0:
          print("Even")
     else:
          print("Odd") 
is_even(12)
is_even(15)

def factorial(n):
     if n==0:
          return 1
     fact=1
     for i in range(1,n+1):
          fact=fact*i
    
     return fact    

print(factorial(5))

def multiplication_table(number):
     print("The multiplication table of ",number,": ")
     for i in range(1,11):
        print(number," * ",i," = ",number*i)  


multiplication_table(7)    

def triangle(rows):
     for i in range(1,rows+1):
      for j in range(1,i+1):
          print("*",end="")
      print()

row=int(input("Enter a positive integer: "))
triangle(row)