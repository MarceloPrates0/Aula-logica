import os
os.system("cls || clear")

def indice_corporal(peso, altura):
    imc = peso / (altura * altura)
    print(f"Seu IMC: {imc:.2f}")
    return imc

def mensagem_imc(numero):
    if numero < 18.5:
        classificacao = "Abaixo do peso  |"
        recomendacao = "\tConsulte um nutricionista para orientação."
    elif numero < 25:
        classificacao = "Peso normal  |"
        recomendacao = "\tMantenha hatitos saudáveis."
    elif numero < 30:
        classificacao = "Sobrepeso  |"
        recomendacao = "\tConsidere uma dieta balanceada e atividade física."
    elif numero < 35:
        classificacao = "Obesidade grau 1  |"
        recomendacao = "\tProcure orentação de uma profissional de saude."
        
    elif numero < 40:
        classificacao = "Obesidade grau 2  |"
        recomendacao = "\tConsulte um médico para avaliação e orientação."    
    else:
        classificacao = "Obesidade grau 3  |"
        recomendacao = "\tBusque assitência médica imediata."
    return classificacao + recomendacao

peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))

imc = indice_corporal(peso, altura)
print(mensagem_imc(imc))