from dataclasses import dataclass
import os
import time
os.system("cls || clear")


lista_nomes = []

# Função que verifica se a lista está vazia 
def verificar_lista_vazia(lista_nomes):
    if not lista_nomes:
        return True
    return False

# Função para adicionar.
def adicionar_nome(lista_nomes):
    nome = input("Digite o nome que deseja adicionar: ")
    lista_nomes.append(nome)
    print(f"\n{nome} adicionado com sucesso.")

# Função para mostrar todos os nomes da lista.
def listar_nomes(lista_nomes):
    if verificar_lista_vazia(lista_nomes):
        return

    print(f"\n - lista de nomes - ")
    for nome in lista_nomes:
        print(f"- {nome}")

# FUnção para atualizar
def atualizar_nome(lista_nomes):
    if verificar_lista_vazia(lista_nomes):
        print("\nA lista está vazia.")
        return
    
    lista_nomes(lista_nomes)
    nome_antigo = input("Digite o nome que deseja atualizar.")
    if nome_antigo in lista_nomes:
        novo_nome = input(f"Digite o novo nome para {nome_antigo}: ")
        indice = lista_nomes.index(nome_antigo)
        lista_nomes[indice] = novo_nome
        print(f"{nome_antigo} foi atualizado para {novo_nome}.")
    else:
        print(f"\nO nome {nome_antigo} não foi encontrado.")



# Função para remover
def excluir_nomes(lista_nomes):
    if verificar_lista_vazia(lista_nomes):
        print("\nA lista está vazia.")
        return
    listar_nomes(lista_nomes)
    nome_remover = input("Digite o nome que deseja remover: ")
    if nome_remover in lista_nomes:
        lista_nomes.remove(nome_remover)
        print(f"{nome_remover} foi removido com sucesso.")
    else:
        print(f"O nome {nome_remover} não foi encontrado.")

# Mostrando menu.
while True:
    print("""
- Gerenciador de nomes -
1 - Adicionar
2 - Listar nomes
3 - Atualizar
4 - Remover                                        
5 - Sair          
""")
    opcao = int(input("Digite uma das opções acima: "))
    match opcao:
        case 1:
            adicionar_nome(lista_nomes)
        case 2:
            listar_nomes(lista_nomes)
        case 3:
            listar_nomes(lista_nomes)
        case 4:
            excluir_nomes(lista_nomes)
        case 5:
            print(f"\nSaindo do algoritmo")
            break
        case _:
            print("\nOpção inválida.")