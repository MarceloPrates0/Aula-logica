import os
os.system ("clear")

idade= int(input("Insira sua idade: "))

if idade < 18 or idade > 65:
    print("Você não tem a obrigação de voto.")
else:
    print("Você é obrigado a votar.")

