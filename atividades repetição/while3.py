import os
os.system("clear")



while True:
    idade = int(input("Insira sua idade: "))
    
    if idade < 18:
        print("Somente maiores de 18 anos.")
    else:
        break

print("\nFIM")
