import os
os.system("cls || clear")

def calcular_media(divisor, dividendo):
    media = divisor / dividendo
    return media
def aprovacao(numero):
    if numero < 7:
        print("Reprovado")
    else:
        print("Aprovado")
        
acumulador = 0
for i in range(1, 4):
    nota = float(input(f"Insira sua {i}ª nota: "))
    acumulador += nota
    
print(f"Sua média foi: {calcular_media(acumulador, i):.2f}")
aprovacao(calcular_media(acumulador, i))