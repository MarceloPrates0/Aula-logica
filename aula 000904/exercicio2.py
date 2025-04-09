import os
from datetime import date
os.system("cls || clear")

def calculo_idade(numero):
    idade = date.today().year - numero
    return idade

idade = int(input("Insira o ano de seu nascimento: "))
print(f"\nVocê possui {calculo_idade(idade)} anos")    