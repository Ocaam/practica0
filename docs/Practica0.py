import pandas as pd
import numpy as np
import sweetviz as sv
import os
print(os.getcwd())

df = pd.read_csv("OneDrive/Escritorio/Master/AprendizajeAuto/practica0/data/Loan_test_set.csv")


# Cargar el archivo CSV
file_path = "OneDrive/Escritorio/Master/AprendizajeAuto/practica0/data/Loan_test_set.csv"  # Ruta del archivo cargado
df = pd.read_csv(file_path, sep=',', low_memory=False, skiprows=1)

# Revisar si hay valores nulos o problemáticos en la columna 'int_rate'
print(df['int_rate'].unique())

# Limpiar la columna 'int_rate': eliminar el símbolo '%' y manejar valores nulos
df['int_rate'] = df['int_rate'].str.rstrip('%')

# Convertir la columna 'int_rate' a float, manejando posibles errores
df['int_rate'] = pd.to_numeric(df['int_rate'], errors='coerce')

# Ahora que la columna 'int_rate' está limpia, generar el análisis con Sweetviz
report = sv.analyze(df)

# Guardar el reporte en un archivo HTML
report.show_html('sweetviz_report.html')



