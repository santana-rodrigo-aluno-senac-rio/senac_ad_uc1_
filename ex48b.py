# Crie uma função que receba dois números e retorne o maior deles ou informe se são iguais.
def maior(a, b):
    if a > b:
        return f"O maior número é: {a}"
    elif a < b:
        return f"O maior número é: {b}"
    else:
        return "Os números são iguais."

# Entrada do usuário
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

# Chamada da função
resultado = maior(n1, n2)

# Exibição do resultado
print(resultado)
