import os
os.system("cls || clear")

def logo_senai():
    os.system("cls || clear")
    print("=== SENAI DENDEZEIROS ===")

def soma(primeiro_numero, segundo_numero):
    return primeiro_numero + segundo_numero

def subtracao(primeiro_numero, segundo_numero):
    return primeiro_numero - segundo_numero

def multiplicacao(primeiro_numero, segundo_numero):
    return primeiro_numero * segundo_numero

def divisao(primeiro_numero, segundo_numero):
    return primeiro_numero / segundo_numero

logo_senai()
primeira_nota = float(input("Insira primeira nota: "))
logo_senai()
segunda_nota = float(input("Insira segunda nota: "))

somando = soma(primeira_nota, segunda_nota) 
subtraindo = subtracao(primeira_nota, segunda_nota) 
multiplicando = multiplicacao(primeira_nota, segunda_nota) 
dividindo = divisao(primeira_nota, segunda_nota) 

logo_senai()
print(f" Sua soma: {somando}")
print(f" Sua subtração: {subtraindo}")
print(f" Sua multiplicação: {multiplicando}")
print(f" Sua divisão: {dividindo}")