import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("Analizis de notas de estudiantes------\n")

#Importar el dataset

try:
    df = pd.read_csv('data/dataset_estudiantes.csv')
    print("\nDataframe cargo exitosamente")
    #mostrar los primeros 5 registros
    print(df.head())

    print("\nEstadisticas descriptivas ")
    print(df.describe())
except FileNotFoundError:
    print("Error: El archivo 'notas_estudiantes.csv' no se encuentra.")

#generar el grafico

plt.figure(figsize=(10,6))
plt.hist(df['nota'], bins=10, color='green', edgecolor='black')
plt.title('Histograma de Notas de Estudiantes')
plt.xlabel('Notas')
plt.ylabel('Frecuencia')
plt.grid(axis='y', alpha=0.75)
plt.axvline(df['nota'].mean(), color='red', linestyle='dashed', linewidth=2, label='Media')
plt.show()    