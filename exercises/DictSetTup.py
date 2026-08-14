student={
    "name":"Imene",
    "age":21,
    "major":"AI"
}
print(student["name"])
print(student["age"])
student["GPA"]=3.9
print(student)
student["major"]="Computer Science"
print(student)
for key,value in student.items():
    print(key , value)

FavCol=input("Enter your favorite color: ")
person= {
    "favorite_color":FavCol
}
print(person)
grades = {
"Math":18,
"Physics":15,
"AI":20,
"English":17
}
total=0
for value in grades.values():
    total += value
average=total / len(grades)
print(average)    

Count=0
for value in grades.values():
    if value >= 16:
        Count+=1
print(Count)    


students={}
std_no=int(input("How many students? "))
for i in range(std_no):
    Name=input("Enter student's name: ")
    Grade=int(input("Enter student's grade"))
    students[Name]=Grade
print(students)    