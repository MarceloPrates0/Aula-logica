import os
os.system ("clear")

idade= int(input("Insira sua idade: "))

if idade < 16:
    print("Você não pode votar.")
elif idade < 17:
    print("Você pode votar, no entando não possui a obrigação.")
elif idade < 65:
    print("Você é obrigado a votar.")
else:
    print("Você pode votar, no entanto não possui a obrigação.")
    
