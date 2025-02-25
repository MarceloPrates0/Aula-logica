import os
os.system ("clear")

# Definições

def calculo_previdencia_social(valor):
    if valor <= 1302:
        imposto = 0.075
    elif valor >= 1302.01 and valor <= 2571.29:
        imposto = (valor * 0.09) - 19.53
    elif valor >= 2571.30 and valor <= 3856.94:
        imposto = (valor * 0.12) - 96.67
    else:
        imposto = (valor * 0.14) - 173.80      
    return imposto
        

def calculo_irrf(valor2):
    if valor2 < 1903.98:
        imposto2 = 0
    elif valor2 >= 1903.99 or valor2 <= 2826.65:
        imposto2 = (valor2 * 0.075) - 142.80
    elif valor2 >= 2826.66 or valor2 <= 3751.05:
        imposto2 = (valor2 * 0.15) - 354.80
    elif valor2 >= 3751.06 or valor2 <= 4664.68:
        imposto2 = (valor2 * 0.225) - 636.18
    else:
        imposto2 = (valor2 * 0.275) - 869.36
    return imposto2                                 

# Propriedades    
       
salario= float(input("Insira seu salário bruto: R$"))
imposto_inss= calculo_previdencia_social(salario)
imposto_irrf= calculo_irrf(salario)
imposto_fgts= salario * 0.08 
liquido= salario - (imposto_inss + imposto_irrf + imposto_fgts)

# Saídas
print("\n===============")
print(f"Estes são seus impostos referentes ao INSS: R${imposto_inss}")
print(f"Estes são seus impostos referentes ao IRRF: R${imposto_irrf}")
print(f"Estes são seus impostos referentes ao FGTS: R${imposto_fgts}")
print("===============")

print(f"\nSeu salário líquido corresponde a: R${liquido}")

