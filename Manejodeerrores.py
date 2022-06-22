# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 10:16:02 2022

@author: user
"""

try:
    numerador = float(input("Numerados:  "))
    denominador = float(input("Denominador:  "))
    resultado = numerador/denominador
    print(f"Resultado: {resultado}")
    print("Gracias")
    
except ZeroDivisionError:
    print("No puedes dividir entre cero....")

except:
    print("Hubo un error")
    
else:
    print("La division se realizo correctamente")
    
finally:
    print("La operacion termino")