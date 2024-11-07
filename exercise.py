import pandas as pd

data_frame1 = {
    'ID:': [1, 2, 3, 4, 5, 6],
    'Name:': ['John', 'Steve', 'Sarah', 'Jane', 'David', 'Samantha'],
}

data_frame2 = {
    'ID:': [1, 2, 3, 4, 5, 6],
    'Age:': [23, 34, 45, 20, 15, 78],
}

df1 = pd.DataFrame(data_frame1) # Criar um DataFrame a partir do dicionário
df2 = pd.DataFrame(data_frame2) # Criar um DataFrame a partir do dicionário

#print(df1)
#print(df2)

merge_data_frame = pd.merge(df1, df2, on='ID:', how='inner') # Unificar os data frames com base no ID
#print(merge_data_frame)

media = merge_data_frame['Age:'].mean() # Calcular a média das idades
#print(media)
moda = merge_data_frame['Age:'].mode() # Calcular a moda das idades
#print(moda)

merge_data_frame['eh_adulto'] = merge_data_frame['Age:'] >= 18 # Adicionar uma nova coluna ao data frame
print("é adulto = ", merge_data_frame['eh_adulto'])

merge_data_frame.reset_index(drop=True, inplace=True) # Resetar o índice do data frame
print(merge_data_frame)

grupo_idades= merge_data_frame.groupby('eh_adulto')['Age:'].mean() # Agrupar as idades
print(grupo_idades)

merge_data_frame = merge_data_frame.sort_values(by='Age:', ascending=False) # Ordenar o data frame
print(merge_data_frame)

