from dataclasses import dataclass
import os
os.system("cls || clear")

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preco: float

    def exibirLivro(self):
        print(f"Livro: {livro1.nome}\nAutor: {livro1.autor}\nCategoria: {livro1.categoria}\nPreço: {livro1.preco}\n")


listaLivro = []
QUANTIDADE_LIVRO = 3
for i in range(QUANTIDADE_LIVRO):
    livro1 = Livro(input("Insira o nome do livro: "),
                   input("Insira o autor do livro: "),
                   input("Insira a categoria do livro: "),
                   int(input("Insira o preço do livro: ")))
    print()
    listaLivro.append(livro1)

arquivo = "dadosLivros.txt"
with open(arquivo, "a", encoding="utf-8") as salva_livro:
    for livro1 in listaLivro:
        salva_livro.write(f"{livro1.nome}, {livro1.autor}, {livro1.categoria}, {livro1.preco}\n")

os.system("cls || clear")
print("===Exibição de livros===")
for livro1 in listaLivro:
    livro1.exibirLivro()