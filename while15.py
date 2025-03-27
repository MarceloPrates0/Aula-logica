import os
os.system ("cls || clear")

contador = 0
acumulador = 0
mulheres_salario_mais5k = 0
idade_maior = 0
idade_menor = 9999


while True:
    permissao = int(input("""
Código  | Descrição
1 \t| Adicionar pessoa
2 \t| Exibir resultados
3 \t| Sair
"""))
    match permissao:
        case 1: 
            os.system("cls || clear")

            # Idade 
            idade = int(input("Insira sua idade: "))
            if idade < idade_menor :
                idade_menor = idade
            if idade > idade_maior:
                idade_maior = idade
            
            # Salario 
            salario = float(input("Insira seu salário: "))
            contador += 1
            acumulador += salario

            # Sexo
            sexo = input("""
Insira seu sexo:
F - Feminino
M - Masculino: 
""").upper()
            match sexo:
                case "M":
                    print()
                case "F":
                    if salario > 4999:
                        mulheres_salario_mais5k += 1
                case _:
                    print("Opção inválida.")

        case 2:
            os.system("cls || clear")
            print(f"Sua idade: {idade}")
            print(f"Seu sexo: {sexo}")
            print(f"Seu salário: {salario}\n")
        case 3:
            break
        case _:
            print("Opção inválida.")

media = acumulador / contador
print(f"A média salarial desse grupo é: {media:.2f}")
print(f"A menor idade é {idade_menor} e a maior idade do grupo é {idade_maior}")
print(f"Possuem {mulheres_salario_mais5k} mulheres com o salário superior a R$5000")