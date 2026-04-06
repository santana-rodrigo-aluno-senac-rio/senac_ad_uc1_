#
#
print("Digite abaixo 03 valores:")
v1=float(input("Digite valor 01: "))
v2=float(input("Digite valor 02: "))
v3=float(input("Digite valor 03: "))
if v1>v2 and v1>v3:
    print(f"O valor maior é: {v1}")
elif v2>v3 and v2>v1:
    print(f"O valor maior é: {v2}")
else:
    print(f"O valor maior é: {v3}")
print("Fim do código")


