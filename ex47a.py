# Crie uma função que receba o lado de um quadrado e retorne o valor de sua área (a = lado^2) (area = lado * lado)
# a =l ** 2

def area(l):
    a = l ** 2
    return a
v = int(input("Digite um valor: "))
y = area(v)
print ("O resultado é: ",y)
print (f"A área do quadrado de lado {v} é igual a {y}")

