'''
Desenvolva um programa que saeja capaz de coletar uma aequencia de 05 numeros inteiros fornecidos pelo usuario.
Ao final da leitura desse svalores, o probgrama deve calcular o somatorio total e exibir o resultado na tela.

'''

soma = 0
for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    soma += numero # equivale a: soma = soma + numero #ou soma = soma +numero
print(f"A soma total dos números fornecidos é: {soma}")
