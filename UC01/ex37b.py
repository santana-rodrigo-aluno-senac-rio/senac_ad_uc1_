i = 0
maior = 0  # Criamos a variável "maior" antes de começar

while i < 3:
    v = int(input("Digite um valor: "))
    
    # Se o valor digitado (v) for maior que o recorde atual (maior)
    if v > maior:
        maior = v  # O novo valor vira o campeão
        
    i = i + 1  # Soma 1 ao contador para não ficar em loop infinito

# O print fica fora do while para mostrar o resultado só no final
print(f"O número maior é: {maior}")