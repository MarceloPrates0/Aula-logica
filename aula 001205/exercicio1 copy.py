import os
import time
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Funcionario:
    nome: str
    dataN: str
    cpf: str
    funcao: str

listaFunci = []

def verificar_lista(listaFunci):
    if not listaFunci :
        return True
    return False

def adicionar(lista):
    funcionario1 = Funcionario(input("Insira seu nome: "),
                               input("Insira sua data de nascimento: "),
                               input("Insira seu CPF: "),
                               input("Insira sua função: "))
    
    lista.append(f"{funcionario1.nome}")
    lista.append(f"{funcionario1.dataN}")
    lista.append(f"{funcionario1.cpf}")
    lista.append(f"{funcionario1.funcao}\n")
    print("===Informações registradas===")


def listar(lista):
    print("===Lista de nomes===")
    for funcionario1 in lista:
        print(f"{funcionario1}")

def atualizar(lista):
    if verificar_lista(listaFunci):
        print("A lista está vazia.")
        return

    listar(listaFunci)
    dado_buscar = input("Insira o dado que deseja atualizar: ")
    if dado_buscar in lista:
        dado_novo = input("Insira o dado para substituir: ")
        indice = lista.index(dado_buscar)
        lista[indice] = dado_novo
        print(f"Atualizado. Espere reiniciar para conferir os dados.")
    else:
        print("Dado não encontrado.")

def remover(lista):
    if verificar_lista(listaFunci):
        print("A lista está vazia.")
        return
    
    nome_remove = input("Insira o dado que deseja remover: ")
    if nome_remove in lista:
        lista.remove(nome_remove)
        print(f"O dado {nome_remove} foi removido com sucesso")
    else:
        print(f"O nome {nome_remove} não foi encontrado.")


while True:
    print("==GERENCIADOS FUNCIONÁRIOS==")
    print("""
1 - Adicionar funcionário
2 - Listar nomes
3 - Atualizar
4 - Excluir
5 - Sair""")
    ordem = int(input("Selecione uma opção: "))
    match ordem:
        case 1:
            adicionar(listaFunci)
        case 2:
            listar(listaFunci)
        case 3:
            atualizar(listaFunci)
        case 4:
            remover(listaFunci)
        case 5:
            break
        case _:
            print("Selecione uma opção válida")
    time.sleep(1.5)
    os.system("cls || clear")



