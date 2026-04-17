# Importa a biblioteca pandas, usada para manipulação e análise de dados
import pandas as pd

# Lê o arquivo CSV chamado 'ClassicDisco.csv' e armazena os dados em um DataFrame (estrutura de dados do pandas)
df = pd.read_csv('ClassicDisco.csv')

# Comando para exibir todo o conteúdo do DataFrame como string (desativado com #)
# Este comando mostra todos os dados do arquivo CSV em formato de string
# print(df.to_string())

# Exibe as primeiras 5 linhas do DataFrame
# Este comando é útil para visualizar as primeiras linhas do arquivo e entender sua estrutura
#print(df.head())

# Exibe as últimas 15 linhas do DataFrame
# Este comando mostra as últimas 15 linhas do arquivo para verificar o final dos dados
#print(df.tail(15))

# Exibe as linhas de índice 10 a 14 (o intervalo é exclusivo no final, ou seja, 15 não é incluído)
# Este comando é útil para visualizar uma parte específica do DataFrame
#print(df[10:15])

# Exibe o formato (shape) do DataFrame
# O comando df.shape retorna uma tupla no formato (número_de_linhas, número_de_colunas)
# Uma tupla é uma estrutura de dados imutável que armazena múltiplos valores em uma única variável.
# Exemplo de saída: (100, 5), onde 100 é o número de linhas e 5 é o número de colunas
print(df.shape)

