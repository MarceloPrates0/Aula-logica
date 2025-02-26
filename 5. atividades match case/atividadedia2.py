import os 
os.system ("clear")

dias= int(input("""
Número \t Dia da semana
1 \t Domingo
2 \t Segunda-feira
3 \t Terça-feira
4 \t Quarta-feira
5 \t Quinta-feira
6 \t Sexta-feira
7 \t Sábado 
Digite o número correspondente ao dia: """))

match dias:
    case 1:
        print("Domingo!")
        print("Fim de semana!")
    case 2:
        print("Segunda-feira!")
        print("Dia útil!")
    case 3:
        print("Terca-feira!")
        print("Dia útil!")
    case 4:
        print("Quarta-feira!")
        print("Dia útil!")
    case 5:
        print("Quinta-feira!")
        print("Dia útil!")
    case 6:
        print("Dia útil!")
    case 7:
        print("Sábado!")
        print("Fim de semana!")
    case _:
        print("Caracter inválido, representa dia nenhum.")