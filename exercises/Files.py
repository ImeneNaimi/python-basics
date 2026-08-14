"""EXO1"""
with open("hello.txt","w") as file:
    file.write("Hello Python! ")
with open("hello.txt","r") as file:
    content=file.read()
print(content)

"""2"""
name=input("Please enter your name: ")
with open("name.txt","w") as f:
    f.write("Hello " + name)    
with open("name.txt","r") as fi:
    cont=fi.read()
print(cont)

"""3"""
with open("numbers.txt","w") as fichier:
    for i in range(1,6):
        fichier.write(str(i) + "\n")
with open("numbers.txt","r") as fichier:
    for line in fichier:
        print(line.strip())

"""4"""
mov1=input("Enter you no 1 favorite movie: ")
mov2=input("Enter you no 2 favorite movie: ")
mov3=input("Enter you no 3 favorite movie: ")
with open("movies.txt","w") as fich:
    fich.write(mov1 + "\n")
    fich.write(mov2 + "\n")
    fich.write(mov3 + "\n")
with open("movies.txt","r") as fich:
    contenu=fich.read()
print(contenu)    


"""5"""
with open("shopping.txt","w") as fil:
    for i in range(5):
        item=input("Enter an item of your shopping list: ")
        fil.write(item + "\n")
with open("shopping.txt","r") as fil:
   print("Shopping list")
   for line in fil:
       print(line.strip())


"""défi"""
with open("NvFichier.txt","w") as NewFile:
    for i in range(5):
        num=input("Entrer un chiffre: ")
        NewFile.write(num + "\n" )
with open("NvFichier.txt","r") as NewFile:
    print("Les chiffres que vous avez entré: ")
    for line in NewFile:
        print(line.strip())        

with open("NvFichier.txt","r") as NewFile:
    somme=0
    for line in NewFile:   
        somme += int(line.strip())
    print("La somme de ces chiffres: ",somme) 

"""challenge1"""
with open("grades.txt","w")as file:
    gradesNo=int(input("How many grades? "))
    for i in range(gradesNo):
        grade=int(input("Enter grade: "))
        file.write(str(grade) + "\n")
with open("grades.txt","r")as file:
    Total=0
    for line in file:
        Total += int(line.strip())
    Average=Total/gradesNo
    print("Total=",Total)
    print("Avreage=",Average)    

"""Challenge2"""
with open("words.txt","w") as fichier:
    for i in range(5):
        word=input("Enter a word: ")
        fichier.write(word + "\n")   
with open("words.txt","r") as fichier:
    for line in fichier:
        if len(line.strip())>5:
         print(line.strip())

"""FINAL BOSS"""
with open("GradeManager.txt","w") as filo:
   studentsNo=int(input("How many students? "))
   for i in range(studentsNo):
      Name=input("Name: ")
      Grade=input("Grade: ")
      filo.write(Name +","+ Grade +"\n")

students={}      
with open("GradeManager.txt","r") as filo:
   for line in filo:
      parts=line.strip().split(",")  
      name = parts[0]
      grade =int(parts[1]) 
      students[name]=grade
      print("Name: ", name , "Grade: ",grade)

highest=max(students,key=students.get)
print("Highest grade: ")
print(highest, "->", students[highest])    
lowest=min(students,key=students.get)
print("Lowest grade: ") 
print(lowest, "->", students[lowest])
Total=0
for value in students.values():
   Total += value
Average=Total/studentsNo
print("Average grade: ",Average) 
