# Calculadora simples em Python

def calculadora():
    print("Selecione a operação:")
    print("1 - Adição (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")

    # Entrada do usuário para escolher a operação
    operacao = input("Digite o número da operação desejada (1/2/3/4): ")

    # Entrada dos números
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Realiza a operação escolhida
    if operacao == '1':
        print(f"O resultado de {num1} + {num2} é {num1 + num2}")
    elif operacao == '2':
        print(f"O resultado de {num1} - {num2} é {num1 - num2}")
    elif operacao == '3':
        print(f"O resultado de {num1} * {num2} é {num1 * num2}")
    elif operacao == '4':
        if num2 != 0:  # Verifica se o divisor não é zero
            print(f"O resultado de {num1} / {num2} é {num1 / num2}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    else:
        print("Operação inválida. Tente novamente.")

# Chamada da calculadora
calculadora()
