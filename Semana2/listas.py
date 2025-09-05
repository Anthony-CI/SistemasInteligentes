# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 17:57:53 2025

@author: UCLAB414
"""

list_num=[1,2,3,4,5,6,7,8,9,10]
list_num=[item for item in range (1,11)]
print(list_num)
list_num2 =[]
for item in range(1,11):
    list_num2[item-1]=item
print(list_num2)

import random
list_num3 =[random.randint(1,200) for_in range(1,11)]
print(list_num3)
print("Menor:",print(min(list_num3)))
print("Mayor:",print(map(list_num3)))
#slicing 
print("2 primeros elementos:" ,list_num3[0:2])
print("2 primeros elementos:",list_num3[:2])
print("2 ultimos elementos:",list_num3[-2:len (list_num3)+1])
print("2 ultimos elementos:",list_num3[-2:])
print("todos los elementos:",list_num3[:])
print("todos los elementos:",list_num3)




"""
crear un diccionario con nombre de estudiantes y sus notas y calcule su promedio
"""
estudiantes ={
    "theylor":[8,8,5,12],
    "Dreyer":[12,15,11,19],
    "Gustavo":[15,19,20,8],
    "Angelina":[5,2,0,20]
    }
#calcular el promedio
valor1,valor2=15,19
print(valor1,valor2)
for nombre, notas in estudiantes.items():
    promedio=sum(notas) / len(notas)
    print(f"Promedio {nombre} es {promedio:.2f}")
    
    
#promedio de todas las notas
todas_las_notas=[]
for notas in estudiantes.values():  
    todas_las_notas.extend(notas)
prom_general= sum(todas_las_notas)/len(todas_las_notas)
print("El promedio de la clase es ", prom_general)

#tupla
"""
Crear una tupla con los días de la semana y mostrar solo los
laborales.
"""
tupla_dias=('Lunes','Martes','Miercoles','Jueves','Viernes','Sábado','Domingo')
print("Dias laborales: ",tupla_dias[0:5])


"""
Funciones
calcule el factorial de un número
"""
def factorial_numero(num):
    if num <0:
        return "El factorial es negativo"
    elif num==0:
        return 1
    else:
        resultado = 1
        for item in range (1,num+1):
            resultado = resultado*item
    return resultado

print ("Factorial de 5 = ", factorial_numero(10))        


#POO

"""
Crear una clase Persona con atributos nombre y edad.

"""

class Persona:
    #constructor de la clase
    def __init__(self,nombre,carrera,edad):
        self.nombre=nombre
        self.carrera= carrera
        self.edad= edad
        
    #Metodos
    def show_info(self):
        print(f"{self.nombre} de la carrera que lleva {self.carrera} tiene {self.edad}")

#instanciar clase
persona1 = Persona("Anderson","ISC",18)
persona1.show_info()







    
    