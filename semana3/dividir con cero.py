# -*- coding: utf-8 -*-
"""
Created on Fri Sep  5 18:45:36 2025

@author: UCLAB414
"""
def dividir(dividendo,divisor):
    
    try:
        cociente = dividendo/divisor
        print(f"El cociente es: {cociente:.2f}")
    except ZeroDivisionError:
        print("el divisor no puede ser cero")
    except TypeError:
        print("Asegurate que tus variables sean numericos")
    except Exception as e:
        print(f"ocurrio un error : {e}")

#llamar a la funcion 

dividir(10, 2)
dividir(10, 0)
dividir(10, 'a')