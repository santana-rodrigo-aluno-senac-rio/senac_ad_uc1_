numeros = []

print("Digite 10 números abaixo:")

for i in range(10):
    # Pedimos o número e o transformamos em um valor inteiro (int)
    valor = int(input(f"Digite o {i+1}º número: "))
    numeros.append(valor)

print("---")
print(f"Os números que você digitou foram: {numeros}")
#
