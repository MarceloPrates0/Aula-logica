import os
os.system("cls || clear")

def media(algarismo_media, algarismo_media2):
    return (algarismo_media + algarismo_media2) / 2

nota1 = float(input("Insira sua primeira nota: "))
nota2 = float(input("Insira sua segunda nota: "))
total = media(nota1, nota2)

def aprovacao(media_total):
    if media_total >= 7:
        print("Aprovado.")
    else:
        print("Reprovado.")
        
aprovacao(total)