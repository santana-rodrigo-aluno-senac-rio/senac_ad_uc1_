#5) Desenvolva um código python para o exercito brasileiro
#onde irá verificar se o candidato está apto a se alista ou 
#não, para se alistar deve ser do sexo masculino e maior de idade.
#
#idade
#gênero
#
#if idade >=18 and gênero == "M":
#
#idade = float(input("Digite sua idade => "))
#g = input("Digite m para masculino ou f para feminino")
#if idade >=18 and g == "m":
#    print("Apto ao alistamento militar")
#else:
#    print("não apto ao alistamento militar")
#
at=int(input("digite ano atual: "))
na=int(input("Digite data de nascimento: "))
g=(input("Digite o genero: "))
idade=(at - na)
if idade >= 18 and g=="m" or g=="M":
    print("Você esta Apto")
else:
    print("Você não esta Apto")



