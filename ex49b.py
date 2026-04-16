def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multi(a, b):
    return a * b

def divi(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero não é permitida."

while True:
    print("\nEscolha uma operação:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")
    
    escolha = input("Digite uma opção: ")
    
    if escolha == "0":
        print("Operação encerrada.")
        break
    
    if escolha not in ["1", "2", "3", "4"]:
        print("Opção inválida. Tente novamente.")
        continue

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite números válidos.")
        continue

    if escolha == "1":
        x = somar(num1, num2)
    elif escolha == "2":
        x = subtrair(num1, num2)
    elif escolha == "3":
        x = multi(num1, num2)
    elif escolha == "4":
        x = divi(num1, num2)

    print(f"O resultado da operação é: {x}")

    