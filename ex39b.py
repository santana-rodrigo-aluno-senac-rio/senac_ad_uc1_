# 1. Definimos qual tabuada queremos
tabuada = int(input("Digite o número da tabuada: "))

# 2. O contador começa em 1 (ou 0, se preferir)
v = 1

print("--- Tabuada do", tabuada, "---")

# 3. O laço vai até 10
while v <= 10:
    resultado = tabuada * v
    
    # Usamos %02d para que o contador e o resultado fiquem alinhados
    print("%d x %02d = %02d" % (tabuada, v, resultado))
    
    # 4. Somamos 1 ao contador para a próxima volta
    v = v + 1