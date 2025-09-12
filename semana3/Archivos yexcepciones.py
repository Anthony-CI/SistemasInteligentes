# -*- cxoding: utf-8 -*-
"""
Created on Fri Sep  5 18:05:08 2025

@author: UCLAB414
"""
import csv

def crear_csv_calcular_total():

    productos = [
        {'producto': 'Manzana', 'precio' : 0.49 },
        {'producto': 'pan', 'precio' : 0.19 },
        {'producto': 'Pepsi', 'precio' : 1.99 },
        {'producto': 'Coca cola', 'precio' : 3.59 },
        {'producto': 'Leche', 'precio' : 4.59 },        
        ]
    #archivo a exportar
    nombre_archivo="productos.csv"
    
    #crear csv
    
    with open(nombre_archivo,mode='w',newline='',encoding='utf-8')as file:
        escribir=csv.DictWriter(file,fieldnames=['producto','precio'])
        escribir.writeheader()
        escribir.writerows(productos)
    print(f"Archivo {nombre_archivo} creado correctamente")
    
    #calcular total de la compra acediendo al csv
    
    precio_total=0
    with open(nombre_archivo,mode='r',newline='',encoding='utf-8') as fila:
        leer = csv.DictReader(fila)
        for row in leer:
            precio_total= precio_total + float(row['precio'])
            
    print(f"precio total de la comprar {precio_total:.2f} soles")


#llamar a la funcion

crear_csv_calcular_total()        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    