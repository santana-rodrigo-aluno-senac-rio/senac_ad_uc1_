v = float(input("Digite o valor do produto: "))

# percentuais de desconto
descontos = [5, 15, 20]

# escolhe a posição do desconto usando contas simples
posicao = (v >= 100) + (v >= 500)

p = descontos[posicao]  # percentual
d = v * (p / 100)       # valor do desconto
vd = v - d              # valor final

print("O valor é R$", v)
print("Desconto: R$", d)
print("Valor final: R$", vd)
print("Seu desconto é de:", p, "%")
#
