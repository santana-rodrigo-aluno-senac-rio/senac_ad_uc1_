#Desenvolva um código python que leia 03 notas e calcúle a média, se a média for maior ou igual a 7, mostre aprovado, se for menor que 6, imprima aprovado, senão imprima recuperação.
#identação

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
if media >= 6:
    print("Aprovado")
else:    print("Recuperação")

