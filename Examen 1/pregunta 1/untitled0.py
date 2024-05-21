# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:41:25 2024

@author: RODO
"""

import csv

# # Ruta del archivo .csv
ruta_archivo = 'mushroom_cleaned.csv'

# # Leer el archivo .csv
with open(ruta_archivo, 'r') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)
        
# Ruta del archivo .csv
# ruta_archivo = 'mushroom_cleaned.csv'

# # Leer el archivo .csv
# with open(ruta_archivo, 'r') as archivo:
#     for linea in archivo:
#         fila = linea.strip().split(',')
#         print(fila)

        
        
import pandas as pd

# Ruta del archivo .csv
# ruta_archivo = 'ruta/del/archivo.csv'

# Leer el archivo .csv
df = pd.read_csv(ruta_archivo)

# Mostrar las primeras 5 filas del DataFrame
print(df.head())
