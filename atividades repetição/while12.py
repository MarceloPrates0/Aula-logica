import os
os.system("cls || clear")

comanda = 0
while True:
    catalogo = int(input("""
    Insira o prato que deseja abaixo:
                        
    Código\t Prato \t\t Valor
    1 \tPicanha\t\t R$25,00
    2 \tLasanha\t\t R$20,00
    3 \tStrogonoff\t R$18,00                                      
    4 \tBife Acebolado\t R$15,00
    5 \tPão com ovo\t R$5,00                         
    """))
    match catalogo:
        case 1:
            prato = 25
        case 2:
            prato = 20
        case 3:
            prato = 18
        case 4:
            prato = 15
        case 5:
            prato = 5
        case _:
            prato = 0
            print("Prato não catalogado no sistema.")

    comanda += prato
    continua = input("Deseja pedir mais um prato? 'S' para sim, 'N' para não: ").upper()
    match continua:
        case "N":
            break
        case "S":
            print()
        case _:
            print("Opção inválida.")
            continua = input("Deseja pedir mais um prato? 'S' para sim, 'N' para não: ").upper()
    os.system("cls || clear")

    
print(f"O total de sua comanda ficou: R${comanda}")


        

