import os
os.system("clear")

idade = 11

print(idade)
if idade < 12:
    print("Acesso negado.")
elif idade < 18:
    print("Somente com permissão dos pais.")    
else:
    print("Acesso permitido.")

print("== FIM ==")