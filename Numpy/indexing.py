import numpy as np
# Indexing d'un tableau 1D

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])
print(arr[1])
print(arr[2])


# Indexing d'une matrice


mat = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(mat[0])       # Première ligne
print(mat[1])       # Deuxième ligne

print(mat[0][1])    # Ligne 0, colonne 1
print(mat[1][2])    # Ligne 1, colonne 2


# Indexing avec ,


print(mat[0, 1])
print(mat[1, 2])


# Sélection de colonnes/lignes


print(mat[:, 1])    # Deuxième colonne
print(mat[0, :])    # Première ligne



# Slicing d'une matrice


print(mat[0:2, 1:3])



# Slicing d'un tableau 1D


arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])
print(arr[:3])
print(arr[2:])
print(arr[::-1])



arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[::2])      # indices 0, 2, 4
print(arr[1::2])     # indices 1, 3, 5


# Sélection conditionnelle


grades = np.array([12, 15, 18, 9, 14, 20, 16, 11, 17, 13])

esgrades = grades[grades >= 15]

print(esgrades)
print("Nombre d'étudiants ayant >= 15 :", len(esgrades))

# Autre méthode :
print("Nombre :", np.sum(grades >= 15))


# Challenge


numbers = np.arange(1, 21)

print(numbers)
print(numbers[1::2])