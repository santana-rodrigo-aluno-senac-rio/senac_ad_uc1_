# Desenvolva um código python que envia um valor para uma função que essa verifique se o número é impar ou par.

# Função para verificar se o número é par ou ímpar
def paridade(numero):
    if numero == 0:
        return "O número 0 não é considerado par nem ímpar."
    elif numero % 2 == 0:
        return "O número é par."
    else:
        return "O número é ímpar."

# Entrada do usuário
valor = int(input("Digite um número para verificar se é par ou ímpar: "))

# Chamada da função e exibição do resultado
resultado = paridade(valor)
print(resultado)


# Este ignora que zero é par ou impar , esta errado mas uso para aprenderentendimento de função e estrutura de decisão.

