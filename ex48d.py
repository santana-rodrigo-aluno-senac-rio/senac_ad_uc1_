def maior(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return None  # Retorna None para indicar que os números são iguais

while True:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    
    resultado = maior(n1, n2)
    
    if resultado is None:  # Caso os números sejam iguais
        print("Os números são iguais. Tente novamente.")
    else:
        print(f"O maior número é: {resultado}.")
        break  # Sai do loop quando os números forem diferentes
    
    