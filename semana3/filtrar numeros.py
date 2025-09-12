# -*- coding: utf-8 -*-
"""
Created on Fri Sep  5 18:59:11 2025

@author: UCLAB414
"""

import random

list_num = [random.randint(1, 200) for _ in range(1,11)]

def sumar(n1,n2):
    return n1+n2

print(sumar(4,5))

sumar1 = lambda n1,n2: n1+n2

print(sumar1(6,4))

#solucion

print(list_num)

validacion =list(map(lambda x: x%2 == 0,list_num))

print(validacion)

pares= list(filter(lambda x: x%2 == 0,list_num))

print(pares)


#comprension de listas 

pares2= [numero for numero in list_num if numero % 2 == 0]
print(pares2)









