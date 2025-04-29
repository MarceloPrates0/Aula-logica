from dataclasses import dataclass
import os
os.system("cls || clear")

# Algoritmo que faz a pessoa inserir um produto e seu preço, calcula os preços e exibe os produtor

@dataclass
class Produto: # 
    nome: str
    preco: int
    # def __init__(self, nome, preco): #
    #     self.nome = nome             #
    #     self.preco = preco           #

QTD = 3
listProd = []
listPreco = []

# Engloba os produtos e preços na respectiva array
for i in range(QTD):
    produto1 = input("Insira o produto: ")
    listProd.append(produto1)
    preco1 = int(input("Insira o preço: "))
    listPreco.append(preco1)

# Cria uma instancia com estrutura de repetição utilizando append em array

produto2 = Produto(listProd, listPreco)

print(f"Preço total dos produtos: R$ {sum(produto2.preco):.2f}") #Exibe o preço total dos produtos
for i, produto2.nome in enumerate(listProd, start=1): #Exibe os produtos inseridos
    print(f"{i}º produto: {produto2.nome}")


