# 1. Definimos a função que saiba somar
def somar(a, b):
    resultado = a + b
    return resultado

# 2. Solicitamos os números ao usuário
try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    
    # 3. Chamamos a função e guardamos o que ela calculou
    total = somar(numero1, numero2)
    
    # 4. Mostramos o resultado na tela
    print(f"A soma de {numero1} e {numero2} é igual a {total}")
except ValueError:
    print("Por favor, insira valores numéricos válidos.")
    