#
#
v=(float(input("Digite o valor do produto: ")))
if v>=500:
   d=(v*0.20)
   vd=v-d #vd valor com desconto
   p=20  
elif v>=100 and v<=499:
   d=(v*0.15)
   vd=v-d 
   p=15
else:
   d=(v*0.05)
   vd=v-d
   p=5
print(f"O valor é R${v} e com desconto de R${d} e o valor final é: R${vd}")
print(f"Seu desconto é de: {p}%")

