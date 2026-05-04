#2) Desenvolva um código que armazene
#a altura de uma pessoa e o peso, calcule o 
#imc OBs use valores reais (float) para a altura
#ao final mostre o Imc
#
p=float(input("Digite seu peso ="))
a=float(input("Digite sua altura ="))
#imc=indice de massa corporal ; #p=peso ; #a=altura
imc = p / (a * a)
print (f"Seu imc é: {imc}")


