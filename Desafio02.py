#Usando a biblioteca pandas, faça alguns filtros  no dataset do link anterior
#Selecione as pessoas vacinadas de Recife do sexo feminino da cor parda e preta maior de 60 anos
#Selecione as pessoas  que se vacinaram nos meses de abril e maio do sexo masculino

import pandas as pd

df_vacinados = pd.read_csv('vacinados.csv')

#Pessoas vacinadas do sexo feminino, de cor parda e preta e maior de 60 anos

df_vacinados1 = df_vacinados.loc[(df_vacinados['sexo'] == 'FEMININO') & (df_vacinados['raca_cor'] == 'PRETA') | (df_vacinados['raca_cor'] == 'PARDA') & (df_vacinados['idade'] > 60)]
filtros1 = df_vacinados1
print(filtros1)

#Pessoas vacinadas nos meses de *abril e maio* do sexo masculino

df_vacinados2 = df_vacinados.loc[(df_vacinados['sexo'] == 'MASCULINO')]
filtros2 = df_vacinados2
print(filtros2)