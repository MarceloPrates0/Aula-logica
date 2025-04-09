import os
os.system("cls || clear")

def indice_corporal(peso, altura):
    imc = peso / (altura * altura)
    return imc

def mensagem_imc(numero):
    if numero < 18.5:
        classificacao = "Abaixo do peso."
        recomendacao = "Consulte um nutricionista para orientação."
    elif numero < 25:
        classificacao = "Peso normal."
        recomendacao = "Mantenha hatitos saudáveis."
    elif numero < 30:
        classificacao = "Sobrepeso."
        recomendacao = "Considere uma dieta balanceada e atividade física."
    elif numero < 35:
        classificacao = "Obesidade grau 1."
        recomendacao = "Procure orentação de uma profissional de saude."
        
    elif numero < 40:
        classificacao = "Obesidade grau 2."
        recomendacao = "Consulte um médico para avaliação e orientação."    
    else:
        classificacao = "Obesidade grau 3."
        recomendacao = "Busque assitência médica imediata."
    return classificacao + recomendacao
    
        
        

peso = float(input("Insira seu peso em quilos: "))
altura = float(input("Insira sua altura em metros: "))





        