import pandas as pd

# Define o caminho do arquivo CSV
# Define the file path to the CSV file
arquivo = "C:\\Users\\User\\sirc24-pandas-python\\glicose-analysis\\glicose_data_suja.csv"

# Lê o arquivo CSV em um DataFrame
# Read the CSV file into a DataFrame
data_frame = pd.read_csv(arquivo)

# Imprime as primeiras 5 linhas do DataFrame
# Print the first 5 rows of the DataFrame
print(data_frame[:5])

# Imprime colunas específicas das primeiras 5 linhas
# Print specific columns of the first 5 rows
print(data_frame[['Dia Semana', 'Data', 'Resultado', 'Dose Insulina', 'kcal', 'carb']].head(5))

# Imprime as linhas de 5 a 10 e colunas de 0 a 2
# Print rows 5 to 10 and columns 0 to 2
print(data_frame.iloc[5:11, 0:3])

# Obtém a primeira linha do DataFrame
# Get the first row of the DataFrame
linha_0_label = data_frame.iloc[0]
# print(linha_0_label)

# Atualiza o valor de 'Resultado' no índice de linha 3
# Update the 'Resultado' value at row index 3
data_frame.at[3, 'Resultado'] = 95

# Imprime a coluna 'Resultado'
# Print the 'Resultado' column
print(data_frame['Resultado'])

# Renomeia a coluna 'Dia Semana' para 'Dia da Semana'
# Rename the column 'Dia Semana' to 'Dia da Semana'
data_frame = data_frame.rename(columns={'Dia Semana': 'Dia da Semana'})

# Ordena o DataFrame pela coluna 'Resultado' em ordem crescente
# Sort the DataFrame by the 'Resultado' column in ascending order
data_frame_order_columns = data_frame.sort_values(by='Resultado', ascending=True)

# Preenche valores ausentes na coluna 'Resultado' com a média da coluna
# Fill missing values in the 'Resultado' column with the mean of the column
data_frame['Resultado'] = data_frame['Resultado'].fillna(data_frame['Resultado'].mean())

# Cria um novo DataFrame com apenas as colunas 'Resultado' e 'kcal'
# Create a new DataFrame with only 'Resultado' and 'kcal' columns
data_frame_novo = data_frame[['Resultado', 'kcal']]

# Calcula a correlação entre 'Resultado' e 'kcal'
# Calculate the correlation between 'Resultado' and 'kcal'
correlacao = data_frame_novo.corr()
print(correlacao)

# Define uma função para classificar os valores de 'Resultado'
# Define a function to classify the 'Resultado' values
def classificar_resultado(resultado):
    if (resultado < 90):
        return 'Baixo'
    elif (resultado <= 120):
        return 'Normal'
    else:
        return 'Alto'

# Aplica a função de classificação à coluna 'Resultado' e cria uma nova coluna 'Classificação'
# Apply the classification function to the 'Resultado' column and create a new column 'Classificação'
data_frame['Classificação'] = data_frame['Resultado'].apply(classificar_resultado)

# Imprime as primeiras 5 linhas das colunas 'Resultado' e 'Classificação'
# Print the first 5 rows of 'Resultado' and 'Classificação' columns
print(data_frame[['Resultado', 'Classificação']].head())

# Filtra os dias com resultados baixos
# Filter the days with low results
dias_resultados_baixos = data_frame[data_frame['Classificação'] == 'Baixo']

data_frame.at[4, 'Dose Insulina'] = 3