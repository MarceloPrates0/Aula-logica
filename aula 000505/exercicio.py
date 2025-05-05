from dataclasses import dataclass
import os
os.system('cls || clear')


@dataclass
class Autor:
    nome: str
    biog: str

@dataclass
class Livro:
    title: str
    ano: int
    autor: Autor

    def exibir_detalhes(self):
        print("===Resultado cadastrado===")
        print(f"Livro inserido: {self.title} | Ano de publicação: {self.ano} | Nome do autor: {self.autor.nome} | Biografia: {self.autor.biog}")

infos = []
informacoes = Livro(input("Insira o título do livro: "),
                    int(input("Insira o ano de lançamento do livro: ")),
                    Autor(input("Insira o nome do autor: "),
                    input("Insira a biografia: ")))
infos.append(informacoes)

arquivo = "Dados.txt"
with open(arquivo, "a") as gravaDado:
    for informacoes in infos:
        gravaDado.write(f"Livro inserido: {informacoes.title} | Ano de publicação: {informacoes.ano} | Nome do autor: {informacoes.autor.nome} | Biografia: {informacoes.autor.biog}\n")

print("===DADOS SALVOS===")

try:
    with open(arquivo, "r") as nome_arquivo:
        linhas = nome_arquivo.readlines()
        for linha in linhas:
            print(f"{linha.strip()}\n")
except FileNotFoundError:
    print("ARQUIVO NÃO ENCONTRADO.")