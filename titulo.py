# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 08:55:22 2022

@author: user
"""

# Problema = necesitamos mostrar los nombres de una cadena
# presentando las primeras letras en mayuscula
# En owrd se conoce como formato titulo

# Importar la libreria

import camelcase

nombre = "humberto julca espillco"

print(nombre.upper())
print(nombre.title())

# Creamos un objeto llamado cam

cam=camelcase.CamelCase()
print("Con camelcase.......")

# Imprimimos el nombre en formatotirulo
# Utilizamos camelcase

print(cam.hump(nombre))

# Para resolver el problema
# Creamos otro objeto llamado cam2
# Al definir el objeto, incluir los argumentos
# 'humberto' y 'julca'

cam2=camelcase.CamelCase('humberto','julca')
print(cam2.hump(nombre))