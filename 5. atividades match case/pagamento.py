import os
os.system ("clear")

valor= float(input("Informe o valor do pagamento: R$"))
forma_pagamento= int(input("""Qual a forma de pagamento?: 
1- A vista
2 - A prazo:
"""))

match forma_pagamento:
    case 1:
        final = valor * 0.1
        parcelas = 1 
        print(f"Você possui um desconto de {final}")
    case 2:
        final = 0
        parcelas= float(input("Insira a quantiade de parcelas: "))
    case _:
        print("Forma de pagamento inválido")

parce = valor/parcelas

match parcelas:
    case 1:
        print("Você pagará ao longo de uma parcela.")
    case 2:
        print("Você pagará ao longo de duas parcelas.")
        print(f"Cada parcela ficará: R${parce:.2f}")
    case 3:
        print("Você pagará ao longo de três parcelas.")
        print(f"Cada parcela ficará: R${parce:.2f}")
    case 4:
        print("Você pagará ao longo de quatro parcelas.")
        print(f"Cada parcela ficará: R${parce:.2f}")
    case 5:
        print("Você pagará ao longo de cinco parcelas.")
        print(f"Cada parcela ficará: R${parce:.2f}")
    case 6:
        print("Você pagará ao longo de seis parcelas.")
        print(f"Cada parcela ficará: R${parce:.2f}")
    case _:
        print("Quantidade de parcelas inválido.")
 
total= valor - final        

print(f"Você pagará no total: R${total}")



