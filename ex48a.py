# Crie uma função que receba dois números e retorne o maior deles.
def maior(a, b):
    if a > b:
        return a
    else:
        return b
# interação com o usuário
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
# retorna função e mostra resultado na tela (printa)
resultado = maior(n1, n2)
print (f"O maior número é: {resultado}.")


