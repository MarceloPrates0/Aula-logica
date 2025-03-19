import os
os.system ("clear")

while True:
    nota = float(input("Insira sua nota: "))
    if nota < 0 or nota > 10:
        nota = float(input("Insira sua nota: "))
    else:
        break

print(f"Sua nota: {nota}.")

       