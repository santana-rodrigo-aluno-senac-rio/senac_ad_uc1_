# Desenvolva um código python que envia um valor para uma função que essa verifique se o número é impar ou par.

# Função para verificar se o número é par ou ímpar
def paridade(numero):
    if numero % 2 == 0:
        return "O número é par."
    else:
        return "O número é ímpar."

# Entrada do usuário
valor = int(input("Digite um número para verificar se é par ou ímpar: "))

# Chamada da função e exibição do resultado
resultado = paridade(valor)
print(resultado)

# def par (a):
#     if a % 2 == 0:
#         r = "par."
#     else:
#         r = "impar."
#v = int(input("Digite um valor: "))
#y=par (v)
#print(y)
#print(f"O número {v} é {par(v)}")
