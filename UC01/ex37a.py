# while , if
# desenvolva um código py que leia, 3 valores, ao final mostre qual é o maior entre os 3.
i = 0
maior = 0
while i < 3:
    v=int(input("Digite um valor: "))
    if v > maior:
        maior = v
    i=i+1
print(f"o número maior é: {maior}")

