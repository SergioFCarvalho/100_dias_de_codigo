# Dado um dataframe df contendo dados de funcionários com as colunas: nomes, departamento e salário. Filtre os funcionários do departamento “TI” e calcule a sua média salarial (Python, Pandas e Numpy)

import pandas as pd
import numpy as np

data = {
    'nome': ['Ana', 'João', 'Pedro', 'Maria', 'Lucas', 'Carla'],
    'departamento': ['TI', 'RH', 'TI', 'Financeiro', 'TI', 'RH'],
    'salario': [5000, 5200, 5200, 6000, 4800, 3300]
}

df = pd.DataFrame(data)

# Filtragem dos funcionários de TI

funcionarios_ti = df[df['departamento'] == 'TI']
print(funcionarios_ti)

# media_salarial
media_salarial = funcionarios_ti['salario'].mean()
# Exibir resultado
print(f'A média salarial dos funcionários de TI é: R$ {media_salarial}')
