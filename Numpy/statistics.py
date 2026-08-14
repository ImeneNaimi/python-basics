import numpy as np
# Statistiques de base


arr = np.array([1, 2, 3, 4, 5])

print("Moyenne :", np.mean(arr))
print("Somme :", np.sum(arr))
print("Maximum :", np.max(arr))
print("Minimum :", np.min(arr))
print("Écart-type :", np.std(arr))



# Exercice 3


numbers = np.array([10, 20, 30, 40, 50])

print("Somme :", np.sum(numbers))
print("Moyenne :", np.mean(numbers))
print("Maximum :", np.max(numbers))
print("Minimum :", np.min(numbers))
print("Écart-type :", np.std(numbers))



# Statistiques sur les notes


grades = np.array([
    12, 15, 18, 9, 14,
    20, 16, 11, 17, 13
])

print("Average :", np.mean(grades))
print("Highest :", np.max(grades))
print("Lowest :", np.min(grades))
print("Standard deviation :", np.std(grades))


# Axis


grades = np.array([
    [2, 4, 6],
    [1, 3, 5],
    [10, 20, 30]
])


# Moyenne de chaque étudiant
print("Moyenne de chaque étudiant :")
print(np.mean(grades, axis=1))


# Moyenne de chaque matière
print("Moyenne de chaque matière :")
print(np.mean(grades, axis=0))


# Maximum de chaque ligne
print("Maximum de chaque ligne :")
print(np.max(grades, axis=1))


# Minimum de chaque colonne
print("Minimum de chaque colonne :")
print(np.min(grades, axis=0))



# Statistiques avec reshape


numbers = np.arange(1, 21)

matrice = numbers.reshape(4, 5)

print("Shape :", matrice.shape)
print(matrice)


# Somme de chaque ligne
print("Somme de chaque ligne :")
print(np.sum(matrice, axis=1))


# Somme de chaque colonne
print("Somme de chaque colonne :")
print(np.sum(matrice, axis=0))


# Moyenne de chaque ligne
print("Moyenne de chaque ligne :")
print(np.mean(matrice, axis=1))


# Moyenne de chaque colonne
print("Moyenne de chaque colonne :")
print(np.mean(matrice, axis=0))



# Challenge : 30 étudiants


grades = np.random.randint(0, 21, size=(30, 5))

print("Shape :", grades.shape)
print(grades)


# Moyenne de chaque étudiant
student_average = np.mean(grades, axis=1)
print("Moyenne de chaque étudiant :")
print(student_average)


# Moyenne de chaque matière
subject_average = np.mean(grades, axis=0)
print("Moyenne de chaque matière :")
print(subject_average)