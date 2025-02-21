import os
os.system ("clear")

idade= int(input("Insira sua idade: "))

if idade <= 6:
    print("Infância")
elif idade <= 9:
    print("Segunda infância")    
elif idade <= 14:
    print("Pré-adolescência")    
elif idade <= 19:
    print("Adolescência")    
elif idade <= 29:
    print("Juventude")    
else:
    print("Adulto")