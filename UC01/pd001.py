import pandas as pd

dados = {'vendedor' : ['Naruto' , 'Goku', 'Seiya'],
         'produto': ['Geladeira', 'Fogão', 'Ar Condicionado'],
         'vendas': [3400, 750, 2650]}

df = pd.DataFrame(dados)
print(df)


'''
print , ver display, display é para jupyter

# read csv porque esta lendo um csv # arq csv são gerados utf-8 é padrao brasileiro # latin1 # delimitador

'''
