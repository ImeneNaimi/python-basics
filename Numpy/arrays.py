import numpy as np

# Création de tableaux

arr = np.array([1, 2, 3, 4, 5])

print("Array :", arr)
print("Shape :", arr.shape)
print("Size :", arr.size)
print("Dtype :", arr.dtype)
print("Dimensions :", arr.ndim)

# Opérations sur les arrays


print(arr * 5)
print(arr / 2)
print(arr + 10)


# Création avec zeros, ones, arange, linspace


array = np.zeros(5)
print(array)

matrix = np.zeros((2, 3))
print(matrix)


arra = np.ones(5)
print(arra)

matri = np.ones((2, 3))
print(matri)


arr = np.arange(1, 6)
print(arr)


tab = np.arange(0, 10, 2)
print(tab)


tabl = np.linspace(0, 10, 5)
print(tabl)



# Opérations entre deux arrays

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(a + b)
print(b - a)
print(a * b)
print(b / a)


# Modification d'une valeur

a[0] = 100
print(a)


# Matrices


mat = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(mat)
print(mat.shape)
print(mat.size)
print(mat.ndim)



# Reshape


arr = np.arange(1, 13)

matrix = arr.reshape(3, 4)
print(matrix)

matrix = arr.reshape(4, 3)
print(matrix)


# Flatten


matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

array = matrix.flatten()
print(array)



# Exercice 1


tableau = np.arange(0, 10)
print(tableau)


# Exercice 2

tb = np.zeros(10)
tbi = np.ones(5)

print(tb)
print(tbi)


# Exercice 4


a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])

print(a + b)
print(b - a)
print(a * b)
print(b / a)