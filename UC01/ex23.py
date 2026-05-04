
mes=input("Digite o nome do mês: ").lower()

if mes in ["dezembro", "janeiro", "fevereiro"]:
    print("verão")
elif mes in ["março", "abril", "maio"]:
   print("Outono")
elif mes in ["junho", "julho", "agosto"]:
   print ("Inverno")
elif mes in ["setembro", "outubro", "novembro"]:
   print("Primavera")
else:
   print("Mês inválido.")




