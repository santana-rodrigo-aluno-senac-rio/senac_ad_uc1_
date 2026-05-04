#Desenvolva um código que o usuário digite o peso e altura e calcule o ima; No final calcule o imc

p=float(input("Digite seu peso ="))
a=float(input("Digite sua altura ="))
imc = p / (a * a)
print (f"Seu imc é: {imc}")

# Outras forma de fazer o mesmo código:

#A altura deve ser digitada em metros, e o código converte para metros antes de calcular o IMC
#p = float(input("Digite seu peso (kg): "))
#a = float(input("Digite sua altura (em metros): "))
##imc = p / (a * a)
#print(f"Seu IMC é: {imc:.2f}")


#Se a altura for digitada em centímetros, o código converte para metros antes de calcular o IMC
#p = float(input("Digite seu peso (kg): "))
#a = float(input("Digite sua altura (em cm): "))
#a = a / 100  # converte para metros
#imc = p / (a * a)
#print(f"Seu IMC é: {imc:.2f}")

#1. Forçar altura em metros (ex: 1.70)
#Verificando se a altura está em um intervalo aceitável:
#Isso evita que a pessoa digite 170 achando que é cm.
#p = float(input("Digite seu peso (kg): "))
#
#while True:
#    a = float(input("Digite sua altura EM METROS (ex: 1.70): "))
#    if 0.5 <= a <= 2.5:
#        break
#    else:
#        print("Altura inválida. Use metros (ex: 1.70).")
#
#imc = p / (a * a)
#print(f"Seu IMC é: {imc:.2f}")


#2. Perguntar a unidade (mais amigável)



