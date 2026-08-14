num=int(input("Enter a number of your choice: "))
if num<0:
    print("This number is negative")
elif num==0:
    print("This number is zero")
else:
    print("This number is postive")

grade=int(input("enter your grade over 100: "))
if 90 <= grade <= 100:
    print("Excellent: ")
elif 70 <= grade <= 89:
    print("Good")
elif 50 <= grade <= 69:
    print("Pass") 
else:
    print("Fail")       

pw=input("Enter your password: ")
if pw=="python123":
    print("Access granted!")
else:
    print("Access denied!")

print("In the next section please enter two numbers of your choice: ")
a=int(input("First number: "))
b=int(input("Second number: "))
if a<b:
    print(b,"is larger than", a)
elif a==b:
    print(a,"is equal to", b)    
else:
    print(a,"is larger than",b)

year=int(input("Enter a year: "))
if year%400==0:
    print("This is a leap year!")
elif year%100==0:
    print("This is not a leap year!")
elif year%4==0:
    print("This is a leap year!")        
else:
    print("This is not a leap year!")   


c=int(input("Enter a number: "))

if c%2==0:
    print("This number is even! ")
else:
    print("This number is odd! ")    

print("In the next section please enter three numbers of your choice: ")
d=int(input("First number: "))
e=int(input("Second number: "))    
f=int(input("Third number: "))
if e<=d and f<=d:
    print(d,"Is the largest!")
elif e<=f and d<=f:
    print(f,"Is the largest!")   
else:
    print(e,"Is the largest!")     