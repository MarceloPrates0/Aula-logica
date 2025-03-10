import os
os.system ("clear")

input("Insira seu nome: ")
nota_um = float(input("Insira sua primeira nota: "))
nota_dois = float(input("Insira suas segunda nota: "))
media = (nota_dois + nota_um)/2

if media < 4:
    media = "E"
    print("Nota E.")
elif media <= 6:
    media = "D"
    print("Nota D.")
elif media <= 7.5:
    media = "C"
    print("Nota C.")
elif media <= 9:
    media = "B"
    print("Nota B.")
else:
    media = "A"
    print("Nota A.")

match media:
    case "E" | "D":
        print("Reprovado.")
    case  "C" | "B" | "A":
        print("Aprovado.")



    




