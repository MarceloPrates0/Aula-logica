import os
os.system("cls || clear")

QtdNotas = []
    
def media(total):   
    return sum(total) / 4

def aprovacao(notas):
    if notas >= 7:
        print("Aprovado.")
    elif notas >= 5:
        print("Recuperação.")
    else:
        print("Reprovado.")

for i in range(4):
    nota = float(input("Insira uma nota: "))
    QtdNotas.append(nota)

print("\n===NOTAS INFORMADAS===")
for nota in QtdNotas:
    print(f"\t{nota}") 


print(f"Sua média: {media(QtdNotas)}")
aprovacao(media(QtdNotas))