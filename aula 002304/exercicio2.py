import os
import time
os.system("cls || clear")

comanda = []
total = 0
prato = ""

while True:
    print("=========CARDÁPIO DIGITAL========")
    print("============SELECIONE============")
    cardapio = int(input("""
CÓDIGO \tPRATO \t\tVALOR
1 \tPICANHA \t25,00
2 \tLASANHA \t20,00
3 \tSTROGONOFF \t18,00
4 \tBIFE ACEBOLADO \t15,00
5 \tPÃO COM OVO \t5,00
"""))
    match cardapio:
        case 1:
            prato = "Picanha | R$25"
            total += 25
        case 2:
            prato = "Lasanha | R$20"
            total += 20
        case 3:
            prato = "Strogonoff | R$18"
            total += 18
        case 4:
            prato = "Bife Acebolado | R$15"
            total += 15
        case 5:
            prato = "Pão com ovo | R$5"
            total += 5
        case _:
            print("Inválido.")
    if cardapio >= 1 or cardapio <= 5:    
        comanda.append(prato)
    permissao = input("Deseja pedir mais algo? S/N: ").upper()
    os.system("cls || clear")    
    if permissao == "N":
        break

print("Processando pedido...")
time.sleep(2)
os.system("cls || clear")
print("===SUA COMANDA===")
for prato in comanda:
    print(prato)

print(f"Total: R${total}")