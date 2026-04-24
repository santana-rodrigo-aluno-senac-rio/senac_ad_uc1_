'''
Desenvolva um código python que entre com a idade e o genero (m ou f).
Se a idade for maior ou igual a 18 e o gênero for m, imprima apto ao alistamento militar.
Senão imprima não apto ao alistamento militar.;
'''

i=int(input("Digite a idade: "))
g=input("Digite o gênero (m ou f): ")
if i >= 18 and g == 'm':
    print("Apto ao alistamento militar.")
else:    print("Não apto ao alistamento militar.")
