import pandas as pd
import sweetviz as sv

ruta_csv = "C:/Users/pablo/OneDrive/Escritorio/Master/AprendizajeAuto/practica0/data/iris.csv"
dataframe= pd.read_csv(ruta_csv)
print(dataframe)

import subprocess
with open('requirements.txt', 'w') as f:
    subprocess.run(['pip', 'freeze'], stdout=f)




