import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
df = pd.read_csv('glicose_data_suja.csv', sep=',', encoding='utf-8', header=None, names=['Dia Semana', 'Data', 'Tipo', 'Resultado', 'Dose Insulina', 'kcal', 'carb', 'Qualidade Sono', 'Col1', 'Col2', 'Col3', 'Col4', 'Col5', 'Col6', 'Col7', 'Col8', 'Col9', 'Col10', 'Col11'])

# Exibir as primeiras linhas do DataFrame para entender a estrutura dos dados
print(df.head())

# Limpar e preparar os dados
# Remover colunas desnecessárias ou vazias
df = df.dropna(axis=1, how='all')

# Preencher valores ausentes com a média da coluna (ou outro método apropriado)
df = df.fillna(df.mean(numeric_only=True))

# Converter colunas para os tipos de dados apropriados
df['Data'] = pd.to_datetime(df['Data'], errors='coerce')
df['Resultado'] = pd.to_numeric(df['Resultado'], errors='coerce')
df['Dose Insulina'] = pd.to_numeric(df['Dose Insulina'], errors='coerce')
df['kcal'] = pd.to_numeric(df['kcal'], errors='coerce')
df['carb'] = pd.to_numeric(df['carb'], errors='coerce')
df['Qualidade Sono'] = pd.to_numeric(df['Qualidade Sono'], errors='coerce')

# Analisar os dados
# Estatísticas descritivas
print(df.describe())

# Agrupar dados por dia da semana e calcular a média dos resultados
mean_by_day = df.groupby('Dia Semana')['Resultado'].mean()
print(mean_by_day)

# Analisar a qualidade do sono
# Agrupar dados por qualidade do sono e calcular a média dos resultados
mean_by_sleep_quality = df.groupby('Qualidade Sono')['Resultado'].mean()
print(mean_by_sleep_quality)

# Classificar os dados
# Classificar por resultado de glicose
df_sorted = df.sort_values(by='Resultado', ascending=False)
print(df_sorted.head())

# Salvar o DataFrame limpo e classificado em um novo arquivo CSV
df_sorted.to_csv('glicose_data_classificada.csv', index=False)

# Análise gráfica
# Histograma dos resultados de glicose
plt.figure(figsize=(10, 6))
plt.hist(df['Resultado'].dropna(), bins=30, edgecolor='k', alpha=0.7)
plt.title('Distribuição dos Resultados de Glicose')
plt.xlabel('Resultado de Glicose')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()

# Média dos resultados de glicose por dia da semana
plt.figure(figsize=(10, 6))
mean_by_day.plot(kind='bar', color='skyblue')
plt.title('Média dos Resultados de Glicose por Dia da Semana')
plt.xlabel('Dia da Semana')
plt.ylabel('Média do Resultado de Glicose')
plt.grid(True)
plt.show()

# Média dos resultados de glicose por qualidade do sono
plt.figure(figsize=(10, 6))
mean_by_sleep_quality.plot(kind='bar', color='lightgreen')
plt.title('Média dos Resultados de Glicose por Qualidade do Sono')
plt.xlabel('Qualidade do Sono')
plt.ylabel('Média do Resultado de Glicose')
plt.grid(True)
plt.show()