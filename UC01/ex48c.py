def maior(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return "Os números são iguais."

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
resultado = maior(n1, n2)
print(f"O maior número é: {resultado}.")
