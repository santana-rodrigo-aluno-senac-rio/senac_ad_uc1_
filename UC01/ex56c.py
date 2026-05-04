"""
Programa que calcula a soma de um intervalo de números inteiros.
Mostra:
1) A soma passo a passo
2) A soma em uma única linha
3) O resultado final formatado

"""

inicio = int(input("Digite o início: "))
fim = int(input("Digite o fim: "))

print("\n" + "=" * 40)
print("SOMA PASSO A PASSO")
print("=" * 40)

soma = 0
i = inicio

while i <= fim:
    print(f"{soma} + {i} = {soma + i}")
    soma += i
    i += 1

print("\n" + "=" * 40)
print("SOMA EM UMA ÚNICA LINHA")
print("=" * 40)

numeros = [str(i) for i in range(inicio, fim + 1)]
expressao = " + ".join(numeros)

print(f"{expressao} = {soma}")

print("\n" + "=" * 40)
print(f"Soma total de {inicio} até {fim}: {soma}")
print("=" * 40)


