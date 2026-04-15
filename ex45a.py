#Criar uma função que calcúle 10% de um valor
def porc(x):
    p = x * 0.1
    return p
v = int(input("Digite um valor: "))
y = porc(v)
print (y)
print (f"10% de {v} é igual a {y}")

