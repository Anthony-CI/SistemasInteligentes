# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 18:33:41 2025

@author: UCLAB414
"""

num1 = int(input("Ingrese primer numero: "))
num2 = int(input("Ingrese segundo numero: "))
operador= input("Ingrese operador(+,-,*,/): ");

if operador == "+":
    resultado = num1+num2
elif operador =="-":
    resultado = num1-num2
elif operador =="*":
    resultado = num1*num2
else:
    if num2 !=0:
        resultado = num1/num2
    else:
        resultado ="error, division por CERO"
print("El resultado es: ",resultado)