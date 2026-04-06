#aula 3
#
#1) Desenvolva um código python que leia 3 notas, calcule a média entre
#as 3 notas.
#Use input e float
#se a media for maior ou igual a 6
#     mostre aprovado
#     senão 
#     mostre recuperação
#
#identação
#n1 = float(input("Digite a nota 1"))
#n2 = float(input("Digite a nota 2"))
#n3 = float(input("Digite a nota 3"))
#m = (n1 + n2 + n3) / 3
#print(f"Sua média é => {m}")
#if m >= 6:
#    print("APROVADO")
#else:
#    print("RECUPERAÇÃO")
#
nota01=float(input("Digite a 1° nota: "))
nota02=float(input("Digite a 2° nota "))
nota03=float(input("Digite a 3° nota "))
media=(nota01+nota02+nota03)/3
print(f"Sua média final é: {media}")
if media >= 6:
    print("APROVADO")
else:
    print("RECUPERAÇÃO")



