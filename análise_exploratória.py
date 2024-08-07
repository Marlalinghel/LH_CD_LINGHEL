# -*- coding: utf-8 -*-
"""Análise_Exploratória.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AxCROkiGvNTlDLTi498ZGSAEDCPOnkJ3

##Nesta seção, exploramos os dados para entender suas principais características e distribuições.##
"""

import pandas as pd

df = pd.read_csv('/content/desafio_indicium_imdb.csv')

print(df.head())

print(df.info())

print(df.describe())

"""##Vamos começar visualizando como os ratings do IMDb estão distribuídos entre os filmes:"""

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
sns.histplot(df['IMDB_Rating'], bins=20, kde=True)
plt.title('Distribuição do IMDb Rating')
plt.xlabel('IMDb Rating')
plt.ylabel('Frequência')
plt.show()

"""O histograma mostra que a maioria dos filmes tem ratings concentrados entre 7.5 e 8.5 no IMDb. Isso indica que a maioria dos filmes no conjunto de dados tende a ter avaliações positivas, com uma média em torno de 7.95.

#Vamos explorar a relação entre a avaliação do IMDb e o meta score usando um gráfico de dispersão:
"""

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Meta_score', y='IMDB_Rating', data=df)
plt.title('Relação entre IMDb Rating e Meta_score')
plt.xlabel('Meta_score')
plt.ylabel('IMDb Rating')
plt.show()

""" O gráfico de dispersão mostra uma correlação positiva entre o meta score e o IMDb Rating. Filmes com meta scores mais altos tendem a ter avaliações mais altas no IMDb, indicando que a crítica influencia positivamente na percepção pública dos filmes."""

filme_recomendado = df.loc[df['IMDB_Rating'].idxmax()]

print(f"Filme recomendado: {filme_recomendado['Series_Title']} ({filme_recomendado['Released_Year']})")
print(f"Gênero: {filme_recomendado['Genre']}")
print(f"Descrição: {filme_recomendado['Overview']}")
print(f"IMDb Rating: {filme_recomendado['IMDB_Rating']}")

"""# Correlação entre variáveis para entender os fatores de faturamento

"""

plt.figure(figsize=(10, 8))

plt.title('Correlação entre Variáveis')
plt.show()

"""#Vamos extrair e visualizar as palavras mais comuns nas sinopses dos filmes para entender os temas predominantes:"""

from sklearn.feature_extraction.text import CountVectorizer

# Extrair palavras-chave da coluna Overview
vectorizer = CountVectorizer(stop_words='english')
overview_matrix = vectorizer.fit_transform(df['Overview'])

# Palavras mais frequentes
palavras = vectorizer.get_feature_names_out()

# Exibir as 10 palavras mais comuns
print("Palavras mais comuns no Overview:")
print(palavras[:10])

"""As palavras mais comuns nas sinopses incluem termos genéricos como "00", "000", "007", entre outros. Isso sugere que precisamos de mais processamento para identificar temas mais específicos."""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Preparar dados para modelagem
X = df[['Meta_score', 'No_of_Votes', 'Gross']]
y = df['IMDB_Rating']

# Dividir dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar modelo de regressão linear
modelo = LinearRegression()


# Salvar o modelo em formato .pkl
import joblib

joblib.dump(modelo, 'modelo_imdb_rating.pkl')
print("Modelo salvo com sucesso!")

"""Para prever a nota do IMDb, utilizamos um modelo de regressão linear com as variáveis Meta_score, No_of_Votes e Gross como preditores. O erro médio quadrático nos permite avaliar o desempenho do modelo na previsão das notas do IMDb."""

import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

"""# Exemplo de preparação e limpeza dos dados"""

df['Gross'] = pd.to_numeric(df['Gross'], errors='coerce')

"""#Tratamento de Valores Ausentes:"""

df['Gross'].fillna(df['Gross'].median(), inplace=True)

"""#Preparação dos Dados para o Modelo:

"""

X = df[['Meta_score', 'No_of_Votes', 'Gross']]
y = df['IMDB_Rating']

"""#Instanciação do Modelo de Regressão Linear:

"""

modelo = LinearRegression()

"""#Salvando o Modelo:"""

nome_arquivo = 'modelo_imdb_rating.pkl'

"""#Carregando o Modelo Salvo:"""

modelo_carregado = joblib.load(nome_arquivo)

"""#Exemplo de Previsão com o Modelo Carregado:"""

exemplo_previsao = [[80.0, 2343110, 28341469]]

from google.colab import files

files.download('modelo_imdb_rating.pkl')