colors= ["red", "blue", "green", "yellow"]
print(colors[0])
print(colors[3])

numbers= [10,20,30,40]
numbers.append(50)
print(numbers)

animals= ["cat","dog","bird"]
animals[1]="rabbit"
print(animals)

fruits= ["apple","banana","orange","grape"]
fruits.remove("banana")
print(fruits)

grades=[]
grades_no=int(input("Enter how many grades: "))
for i in range(grades_no):
    grade=int(input("Enter the grade: "))
    grades.append(grade)
print(grades)
total=0
for grade in grades:
    total+=grade
print("The total og these grades is: ",total)

average=total/len(grades)
print("The average of these grades is: ",average)

numeros= [8, 15, 3, 22, 9]
maximum=numeros[0]
for numero in numeros:
    if maximum<numero:
        maximum=numero
print("The list:",numeros)
print("the largest number is of this list is: ",maximum) 

numbers = [1, 4, 7, 10, 13, 18]
even_no=0
for number in numbers:
    if number%2==0:
        even_no +=1
print(numbers)
print("The number of even numbers in this list: ",even_no)        

Nums_List=[]
for i in range(10):
   Nums_List.append(int(input("Enter a number: ")))
print("Original list: ")    
print(Nums_List)   
even_only=[] 
for Num in Nums_List:
    if Num%2==0:
        even_only.append(Num)
print("Even: ")
print(even_only)
