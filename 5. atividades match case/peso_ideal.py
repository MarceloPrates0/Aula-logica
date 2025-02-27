import os 
os.system ("clear")

genero= input("""
Masculino - M
Feminino - F
Selecione o gênero de sua escolha para saber seu peso ideal:
""")  

match genero:
    case "M":
        altura= float(input("Insira sua altura: "))
        imc= (72.7 * altura) - 58
        print(f"Seu peso ideal é: {imc:.2f}")
    case "F":
        altura2= float(input("Insira sua altura: "))
        imc2= (62.1 * altura2) - 44.7
        print(f"Seu peso ideal é: {imc2:.2f}")
