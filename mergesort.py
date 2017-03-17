# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 18:06:06 2017

@author: personal
"""

#array para ordenar
A  = [2, 4, 5, 7, 1, 2, 3, 6]
print(A)
#estableciendo indices pertinentes para este algoritmo
p, q, r = 0, (len(A)//2) - 1, len(A) - 1

#calculando la longitud del subarray A[p..q]
n1 = q - p + 1

#calculando la longitud del subarray A[q+1..r]
n2 = r - q

#creando array izquierda
L = []
#creando array derecha
R = []

#creando el array que contiene los elementos de la mitad izq
for i in range(0, n1):
    L.append(A[p + i])

#creando el array que contiene los elementos de la mitad der
for i in range(0, n2 ):
    R.append(A[q + 1 + i])
    
#agregando sentinelas
L.append(1000), R.append(1000)

#declarando indices que se recorreran de manera discontinua mientras
#se ejeccuta el ordenamierto
i, j = 0, 0

#ordenando
for k in range(p, r + 1):
    if L[i] <= R[j]:
        A[k] = L[i]
        i = i + 1
    else:
        A[k] = R[j]
        j = j + 1
   

print(A)
