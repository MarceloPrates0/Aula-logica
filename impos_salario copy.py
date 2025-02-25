import os
os.system ("clear")

def calcular_inss (valor_salario): # INSS críterio de análise
    if valor_salario <= 1212:
        porcentual_desconto_inss = 7.5
    elif valor_salario >= 1212.01 and valor_salario < 2427.35:
        porcentual_desconto_inss = 9
    elif valor_salario >= 2427.36 and valor_salario < 3641.03:
        porcentual_desconto_inss= 12
    elif valor_salario >= 3641.04:
        porcentual_desconto_inss = 14
    return round(valor_salario * porcentual_desconto_inss / 100.0, 2)

def calcular_ir (valor_salario, a): # IR críterio de análise

    base_ir = round(valor_salario - a, 2)
    # print('Base para calculo IR', base_ir)

    if base_ir <= 1903.98:
        return 0
    elif base_ir >= 1903.99 and base_ir < 2826.65:
        porcentagem_desconto_ir = 7.5
        deducao_imposto = 142.80
    elif base_ir >= 2826.66 and base_ir < 3751.05:
        porcentagem_desconto_ir = 15
        deducao_imposto = 354.80
    elif base_ir >= 3751.05 and base_ir < 4664.68:
        porcentagem_desconto_ir = 22.5
        deducao_imposto = 636.13
    elif base_ir >= 4664.68:
        porcentagem_desconto_ir = 27.5
        deducao_imposto = 869.36
    return round((base_ir * porcentagem_desconto_ir / 100.0) - deducao_imposto,2)

valor_salario = float(input('Qual é o valor do seu salário bruto? ')) # varíavel para salário bruto

a = calcular_inss(valor_salario)
b = calcular_ir(valor_salario, a)
c = valor_salario

print('Valor INSS: R$', a)
print('Valor IR: R$', b)
# print('valor bruto R$', c)
# print(type(a))
# print(type(b))
# print(type(c))

# calculos para análise
d = a + b
e = round(c - d, 2)

# print(d)
print('Valor salário líquido: R$', e)