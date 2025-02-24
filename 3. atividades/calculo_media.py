import os
os.system ("clear")

var1 = float(input('Insira sua primeira média: '))
var2 = float(input('Insira sua segunda média: '))
var3 = float(input('Insira sua terceira média: '))

media= (var1 + var2 + var3) / 3

print(f"Sua média é: {media}")

if media >= 7:
    print("Aprovado!")
else:
    print("Reprovado.")    


