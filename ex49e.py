# Calculadora simples em Python

# Função principal da calculadora
def calculadora():
    while True:  # Loop principal para manter a calculadora funcionando até o usuário sair
        # Exibe o menu de operações
        print("\nSelecione a operação:")
        print("1 - Adição (+)")
        print("2 - Subtração (-)")
        print("3 - Multiplicação (*)")
        print("4 - Divisão (/)")
        print("0 - Sair")  # Opção para encerrar a calculadora
        
        # Entrada do usuário para escolher a operação
        operacao = input("Digite o número da operação desejada (1/2/3/4/0): ")
        
        # Verifica se o usuário escolheu sair
        if operacao == '0':
            print("Calculadora encerrada.")  # Mensagem de encerramento
            break  # Sai do loop e encerra o programa
        
        # Verifica se a operação escolhida é válida
        if operacao not in ['1', '2', '3', '4']:
            print("Operação inválida. Tente novamente.")  # Mensagem de erro
            continue  # Volta ao início do loop para pedir uma nova operação
        
        # Tenta obter os números do usuário
        try:
            num1 = float(input("Digite o primeiro número: "))  # Primeiro número
            num2 = float(input("Digite o segundo número: "))  # Segundo número
        except ValueError:  # Captura erros caso o usuário insira algo que não seja um número
            print("Entrada inválida. Por favor, digite números válidos.")  # Mensagem de erro
            continue  # Volta ao início do loop para pedir novamente
        
        # Realiza a operação escolhida
        if operacao == '1':  # Adição
            print(f"O resultado de {num1} + {num2} é {num1 + num2}")
        elif operacao == '2':  # Subtração
            print(f"O resultado de {num1} - {num2} é {num1 - num2}")
        elif operacao == '3':  # Multiplicação
            print(f"O resultado de {num1} * {num2} é {num1 * num2}")
        elif operacao == '4':  # Divisão
            if num2 != 0:  # Verifica se o divisor não é zero
                print(f"O resultado de {num1} / {num2} é {num1 / num2}")
            else:
                print("Erro: Divisão por zero não é permitida.")  # Mensagem de erro para divisão por zero

# Chamada da função calculadora
calculadora()
