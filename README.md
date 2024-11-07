# Glicose Data Analysis

Este projeto foi desenvolvido durante o evento SIRC XVI Simpósio de Informática - UFN - 2024, no curso "Fundamentos de Programação Pandas para análise e manipulação de dados em Python". O objetivo do projeto é realizar a análise e manipulação de dados de glicose utilizando a biblioteca Pandas em Python.


## Descrição dos Arquivos

- **exercise.py**: Contém exemplos de manipulação de DataFrames utilizando Pandas, como unificação de DataFrames, cálculo de média e moda, adição de novas colunas, agrupamento e ordenação de dados.

- **glicose-analysis/achive_manipulation.py**: Script responsável por ler, manipular e analisar dados de glicose a partir de um arquivo CSV. Inclui operações como renomear colunas, preencher valores ausentes, calcular correlações e classificar resultados.

- **glicose-analysis/glicose-data-analyst.py**: Script principal para análise de dados de glicose. Realiza a leitura do arquivo CSV, limpeza e preparação dos dados, análise descritiva, agrupamento por dia da semana e qualidade do sono, classificação dos dados e geração de gráficos.

- **glicose-analysis/glicose_data_suja.csv**: Arquivo CSV contendo os dados brutos de glicose.

- **glicose-analysis/glicose_data_classificada.csv**: Arquivo CSV gerado após a limpeza e classificação dos dados.

## Funcionalidades Implementadas

1. **Leitura e Preparação dos Dados**:
   - Leitura do arquivo CSV contendo os dados de glicose.
   - Remoção de colunas desnecessárias ou vazias.
   - Preenchimento de valores ausentes com a média das colunas.
   - Conversão de colunas para os tipos de dados apropriados.

2. **Análise Descritiva**:
   - Cálculo de estatísticas descritivas dos dados.
   - Agrupamento dos dados por dia da semana e cálculo da média dos resultados de glicose.
   - Agrupamento dos dados por qualidade do sono e cálculo da média dos resultados de glicose.

3. **Classificação e Salvamento dos Dados**:
   - Classificação dos dados por resultado de glicose.
   - Salvamento do DataFrame limpo e classificado em um novo arquivo CSV.

4. **Análise Gráfica**:
   - Geração de histogramas para visualizar a distribuição dos resultados de glicose.
   - Geração de gráficos de barras para visualizar a média dos resultados de glicose por dia da semana e por qualidade do sono.

## Exemplo de Código

Aqui está um exemplo de código do arquivo `glicose-analysis/glicose-data-analyst.py`:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
df = pd.read_csv('glicose_data_suja.csv', sep=',', encoding='utf-8', header=None, names=['Dia Semana', 'Data', 'Tipo', 'Resultado', 'Dose Insulina', 'kcal', 'carb', 'Qualidade Sono', 'Col1', 'Col2', 'Col3', 'Col4', 'Col5', 'Col6', 'Col7', 'Col8', 'Col9', 'Col10', 'Col11'])

# Limpar e preparar os dados
df = df.dropna(axis=1, how='all')
df = df.fillna(df.mean(numeric_only=True))
df['Data'] = pd.to_datetime(df['Data'], errors='coerce')
df['Resultado'] = pd.to_numeric(df['Resultado'], errors='coerce')
df['Dose Insulina'] = pd.to_numeric(df['Dose Insulina'], errors='coerce')
df['kcal'] = pd.to_numeric(df['kcal'], errors='coerce')
df['carb'] = pd.to_numeric(df['carb'], errors='coerce')
df['Qualidade Sono'] = pd.to_numeric(df['Qualidade Sono'], errors='coerce')

# Analisar os dados
print(df.describe())
mean_by_day = df.groupby('Dia Semana')['Resultado'].mean()
print(mean_by_day)
mean_by_sleep_quality = df.groupby('Qualidade Sono')['Resultado'].mean()
print(mean_by_sleep_quality)

# Classificar os dados
df_sorted = df.sort_values(by='Resultado', ascending=False)
print(df_sorted.head())
df_sorted.to_csv('glicose_data_classificada.csv', index=False)

# Análise gráfica
plt.figure(figsize=(10, 6))
plt.hist(df['Resultado'].dropna(), bins=30, edgecolor='k', alpha=0.7)
plt.title('Distribuição dos Resultados de Glicose')
plt.xlabel('Resultado de Glicose')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
mean_by_day.plot(kind='bar', color='skyblue')
plt.title('Média dos Resultados de Glicose por Dia da Semana')
plt.xlabel('Dia da Semana')
plt.ylabel('Média do Resultado de Glicose')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
mean_by_sleep_quality.plot(kind='bar', color='lightgreen')
plt.title('Média dos Resultados de Glicose por Qualidade do Sono')
plt.xlabel('Qualidade do Sono')
plt.ylabel('Média do Resultado de Glicose')
plt.grid(True)
plt.show()
```

## Requisitos
* Python 3.x
* Pandas
* Matplotlib

## Como Executar
1. Clone o repositório:

~~~git clone https://github.com/seu-usuario/glicose-data-analysis.git
cd glicose-data-analysis
~~~

2. Crie um ambiente virtual e ative-o:

~~~python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
~~~

3. Instale as dependências:

~~~pip install pandas matplotlib
~~~

4. Execute os scripts:

```python glicose-analysis/glicose-data-analyst.py
python glicose-analysis/achive_manipulation.py
```

## Autor
Desenvolvido por Kristian Frasson durante o SIRC XVI Simpósio de Informática - UFN - 2024.


### Passos para Adicionar ao GitHub

1. Crie um novo repositório no GitHub com o nome `glicose-data-analysis`.
2. Clone o repositório para o seu ambiente local.
3. Adicione os arquivos do projeto ao repositório clonado.
4. Adicione o arquivo [README.md](http://_vscodecontentref_/1) ao repositório.
5. Faça commit e push das alterações para o GitHub.

```bash
git clone https://github.com/seu-usuario/glicose-data-analysis.git
cd glicose-data-analysis
# Adicione os arquivos do projeto
git add .
git commit -m "Initial commit with project files"
git push origin main


