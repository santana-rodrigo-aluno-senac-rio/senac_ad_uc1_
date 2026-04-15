# Função para calcular qualquer porcentagem de um valor
def porc(valor, porcentagem):
    resultado = valor * (porcentagem / 100)
    return resultado

# Entrada do usuário
v = float(input("Digite um valor: "))
p = float(input("Digite a porcentagem que deseja calcular: "))

# Chamada da função
resultado = porc(v, p)

# Exibição do resultado
print(f"{p}% de {v} é igual a {resultado}")
