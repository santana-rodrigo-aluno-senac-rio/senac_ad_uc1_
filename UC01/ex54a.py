'''
Desenvolva um código python que leia o salário de um funcionário se o salário for maior que R$ 5000,00
Calcule o irrf que será 7,5% sobre o salário
Se for menor que 5000 não paga imposto ir.
E se for mIOR QUE 8000,00 o imposto será 27%. Ao final mostre: o salário, o valor do imposto pago e salário final.
regras:
1 - <= 5000 imposto = 0
2 - > 5000 até 8000 imposto 7,5%
3 - > 8000 imposto 27%
'''

salario=float(input("Digite o seu sálario: "))
if salario <= 5000:
   irrf=(salario*00) 
   salariofinal=salario-irrf
   #ir=input("isento")
   ir=0
elif salario > 5000 and salario <= 8000:
   irrf=(salario*7.5)/100 #7,5%
   salariofinal=salario-irrf
   ir=7.5
else:
   irrf=(salario*27)/100 # 27%
   salariofinal=salario-irrf
   ir=27
print(f"Seu salário atual é: R$ {salario}; O valor a pagar é: R$ {irrf}")
print(f"Imposto pago:{ir}%; Salário final: R$ {salariofinal}")
