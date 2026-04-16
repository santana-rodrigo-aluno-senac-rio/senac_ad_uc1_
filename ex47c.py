# Função que calcula o quadrado de um número
def potencia(base):
    resultado = base ** 2  # Expoente fixo em 2
    return resultado

# Entrada do usuário
base = int(input("Digite o valor da base: "))

# Chamada da função
resultado = potencia(base)

# Exibição do resultado
print(f"O resultado de {base} elevado a 2 é {resultado}")