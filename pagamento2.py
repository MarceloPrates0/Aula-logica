import os
os.system ("clear")

pagamento = float(input("Insira o valor total de seu pagamento:"))
forma_pagamento = float(input("""
1 - A vista
2 - A prazo                              
Insira a forma de pagamento: """))

if forma_pagamento == 1:
    desconto = pagamento * 0.1
else:
    desconto = 0
credito = int(0)
match forma_pagamento:
    case 1:
        total_pagar= pagamento - desconto
        print("Pagamento à vista")
        print(f"Seu desconto é de {desconto:.2f}")
        print(f"Seu total a pagar com o desconto será: R${total_pagar:.2f}")   
    case 2:
        print("Pagamento à prazo")
        credito= int(input("Insira a quantidade de parcelas"))    
    case _:
        print("Opção inválida")

match credito:
    case 0:
        print("Seu pagamento foi computado à vista")
    case 1:
        parcela= pagamento/credito
        print("Você pagará ao longo de uma parcela")
        print(f"Valor total da parcela: R${parcela:.2f}")
        print(f"Total à prazo: R${pagamento}")        
    case 2:
        parcela= pagamento/credito
        print("Você pagará ao longo de duas parcelas")
        print(f"Valor total da parcelas: R${parcela:.2f}")
        print(f"Total à prazo: R${pagamento}")        
    case 3:
        parcela= pagamento/credito
        print("Você pagará ao longo de três parcelas")
        print(f"Valor total da parcelas: R${parcela:.2f}")
        print(f"Total à prazo: R${pagamento}")        
    case 4:
        parcela= pagamento/credito
        print("Você pagará ao longo de quatro parcelas")
        print(f"Valor total da parcelas: R${parcela:.2f}")
        print(f"Total à prazo: R${pagamento}")        
    case 5:
        parcela= pagamento/credito
        print("Você pagará ao longo de cinco parcelas")
        print(f"Valor total da parcelas: R${parcela:.2f}")
        print(f"Total à prazo: R${pagamento}")        
    case 6:
        parcela= pagamento/credito
        print("Você pagará ao longo de seis parcelas")
        print(f"Valor total da parcelas: R${parcela:.2f}")
        print(f"Total à prazo: R${pagamento}")
    case _:
        print("Número inválido de parcelas.")



        
     