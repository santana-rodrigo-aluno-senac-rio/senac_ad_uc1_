# Usando while, desenvolva um cod em  py que some os numeros de 1 a 100


i = 1          # Contador (começa no 1)
soma = 0       # Acumulador (começa vazio)

while i <= 100:
    soma = soma + i  # Pega o que já tem na soma e adiciona o valor atual de i
    i = i + 1        # Passa para o próximo número

print("A soma de 1 até 100 é:", soma) # O resultado da soma de 1 a 100 é 5050.

