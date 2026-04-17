# Jogo de adivinhação

import random  # Importa o módulo para gerar números aleatórios

def jogo_adivinhacao():
    print("Bem-vindo ao jogo de adivinhação!")
    numero_secreto = random.randint(1, 100)  # Gera um número aleatório entre 1 e 100
    tentativas = 0  # Contador de tentativas

    while True:
        try:
            chute = int(input("Digite um número entre 1 e 100: "))  # Entrada do usuário
            tentativas += 1  # Incrementa o número de tentativas

            if chute < 1 or chute > 100:  # Verifica se o número está fora do intervalo
                print("Por favor, digite um número entre 1 e 100.")
                continue

            if chute < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif chute > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                break  # Sai do loop quando o número for adivinhado
        except ValueError:  # Captura entradas inválidas
            print("Entrada inválida. Por favor, digite um número válido.")

# Chamada do jogo
jogo_adivinhacao()
