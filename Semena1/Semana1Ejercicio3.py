# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 18:48:19 2025

imprimer la tabla de multiplicar de un numero dado
"""
flag = True
while flag:
    num3 = int(input("Ingrese un numero entre 1 y 9: "))
    if num3>=1 and num3<=9:
        flag = False
        print("Numero correcto")

print("Tabla de multiplicar con for")
for item in range(1,13):
    print(num3, " X " , item, " = ", num3*item)

print()
print("Tabla de multiplicar con WHILE")
contador = 1
while contador <=12:
    print(num3, " X " , contador, " = ", num3*contador)
    contador = contador+1