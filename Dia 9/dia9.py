# Dado um dataframe df contendo dados de vendas, calcule e exiba: media, mediana, desvio padrão, máximo e mínimo da coluna numérica “vendas” (Python, Pandas e Numpy)

import pandas as pd
import numpy as np

data = {'vendas': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]}

df = pd.DataFrame(data)

# Operações
media = df['vendas'].mean()
mediana = df['vendas'].median()
desvio_padrao = df['vendas'].std()
maximo = df['vendas'].max()
minimo = df['vendas'].min()

# Resultados
print("Média:", media)
print("Mediana:", mediana)
print("Desvio Padrão:", desvio_padrao)
print("Máximo:", maximo)
print("Mínimo:", minimo)
