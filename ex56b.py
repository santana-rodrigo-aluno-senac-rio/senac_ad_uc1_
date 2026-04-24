inicio = int(input("Digite o início: "))
fim = int(input("Digite o fim: "))

soma = 0
i = inicio

print("\nSomando os valores:")

while i <= fim:
    soma += i
    print(f"{soma - i} + {i} = {soma}")
    i += 1

print(f"\n✅ Soma total de {inicio} até {fim}: {soma}")