import os
os.system("clear")

dia= input("Digite o dia da semana: ")

match dia:
    case "segunda-feira" | "segunda" | "Segunda"| "Segunda-feira":
        print("Hoje é segunda-feira")
    case "terça-feira" | "Terça-feira" | "Terça" | "terça":
        print("Hoje é terça-feira")
    case "quarta-feira" | "Quarta-feira" | "Quarta" | "quarta":
        print("Hoje é quarta-feira")
    case "quinta-feira" | "Quinta-feira" | "quinta" | "Quinta":
        print("Hoje é quinta-feira")
    case "sexta-feira" | "Sexta-feira" | "Sexta" | "sexta":
        print("Hoje é sexta-feira")
    case "sabado" | "domingo" | "Sabado" | "Domingo":
        print("Hoje é fim de semana")
    case _:
        print("Dia inválido")

print("=== FIM ===")

