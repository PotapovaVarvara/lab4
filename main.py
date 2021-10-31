# 6. Дан двумерный массив случайных чисел MxM. Вычислить определитель (детерминант) матрицы.

import random
import copy


def getMinor(A, i, j):
    M = copy.deepcopy(A)
    del M[i]
    for i in range(len(A[0]) - 1):
        del M[i][j]
    return M


def getDet(A):
    m = len(A)
    n = len(A[0])
    if m != n:
        return None
    if n == 1:
        return A[0][0]
    signum = 1
    determinant = 0
    # разложение по первой строке
    for j in range(n):
        determinant += A[0][j] * signum * getDet(getMinor(A, 0, j))
        signum *= -1
    return determinant


def print_matrix(a):
    for k1 in range(len(a)):
        for k2 in range(len(a[k1])):
            print(a[k1][k2], end=' ')
        print()


n = random.randint(2, 5)
arr = []

# create a matrix
for i in range(n):
    arr.append([0] * n)

# fill the matrix
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = random.randint(0, 5)

print_matrix(arr)

print("Визначник матриці: ")
print(getDet(arr))
