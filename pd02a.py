import pandas as pd

dados = {
    'cargos': ["assistente", "analista", "gerente", "diretor"],
    'salarios': [1000, 2000, 3000, 4000]
    }

dados_bi = pd.DataFrame(dados)
print(dados_bi)


#print(dados_bi.head(2))
#print(dados_bi.tail(2))
#print(dados_bi[2:4])
#print(dados_bi.shape)


#print(dados_bi, "\n")  # Adiciona uma linha em branco após a impressão

#print(dados_bi.head(2), "\n")  # Adiciona uma linha em branco após as primeiras 2 linhas

#print(dados_bi.tail(2), "\n")  # Adiciona uma linha em branco após as últimas 2 linhas

#print(dados_bi[1:2], "\n")  # Adiciona uma linha em branco após a linha de índice 1

#print(dados_bi.shape, "\n")  # Adiciona uma linha em branco após o formato do DataFrame
#print(dados_bi.shape, end="\n\n")


# Exportando o DataFrame para um arquivo CSV
dados_bi.to_csv('meus_dados.csv', index=False, sep=';' ,encoding='utf-8')

print("Arquivo CSV 'meus_dados.csv' exportado com sucesso!")

