# Função que calcula a potência de um número
def potencia(base, expoente):
    resultado = base ** expoente
    return resultado

# Entrada do usuário
base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))

# Chamada da função
resultado = potencia(base, expoente)

# Exibição do resultado
print(f"O resultado de {base} elevado a {expoente} é {resultado}")
