import os
os.system ("clear")

# Definições

def calculo_previdencia_social(valor):
    if valor <= 1302:
        imposto = (valor * 0.075)
    elif valor >= 1302.01 and valor <= 2571.29:
        imposto = (valor * 0.09) - 22.77
    elif valor >= 2571.30 and valor <= 3856.94:
        imposto = (valor * 0.12) - 106.59
    else:
        imposto = (valor * 0.14) - 190.40   
    return imposto



def calculo_irrf(valor2):
    if valor2 < 1903.98:
        imposto2 = 0
    elif valor2 >= 1903.99 or valor2 <= 2826.65:
        imposto2 = (valor2 * 0.075) - 169.44
    elif valor2 >= 2826.66 or valor2 <= 3751.05:
        imposto2 = (valor2 * 0.15) - 381.44
    elif valor2 >= 3751.06 or valor2 <= 4664.68:
        imposto2 = (valor2 * 0.225) - 662.77
    else:
        imposto2 = (valor2 * 0.275) - 896.00
    return imposto2 


def calculo_fgts(fundo_garantia):
    if fundo_garantia <= 1000: # Faixa salarial de jovem aprendiz
        imposto_fgts= fundo_garantia * 0.02 # FGTS so recai em 2% no salário de jovem aprendiz.
    else:
        imposto_fgts= fundo_garantia * 0.08
    return imposto_fgts         

# Propriedades    
       
salario= float(input("Insira seu salário bruto: R$"))
imposto_inss= calculo_previdencia_social(salario)
# liquido_inss= salario - imposto_inss  
imposto_irrf= calculo_irrf(salario)
calcular_fgts= calculo_fgts(salario)
liquido= salario - (imposto_inss + imposto_irrf + calcular_fgts)

# Saídas
print("\n====================================================")
print(f"Estes são seus impostos referentes ao INSS: R${imposto_inss:.2f}")
print(f"Estes são seus impostos referentes ao IRRF: R${imposto_irrf:.2f}")
print(f"Estes são seus impostos referentes ao FGTS: R${calcular_fgts:.2f}")
print("====================================================")

print(f"\nSeu salário líquido corresponde a: R${liquido:.2f}")

