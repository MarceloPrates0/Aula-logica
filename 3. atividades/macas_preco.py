import os
os.system ("clear")

print("===========================================")
print("Cada maçã custa R$1,30, R$1 A PARTIR DE 12!")
print("===========================================")

macas= float(input("\nQuantas unidades irá querer?: "))
uni= 1.3

if macas > 12:
    uni = 1

mult= uni * macas
total = round(mult, 2)

print(f"Essa quantidade de maçãs dará: R${total}")
