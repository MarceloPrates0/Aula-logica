from dataclasses import dataclass
import os
os.system("cls || clear")

@dataclass
class Brasileiro:
    nome: str
    dataN: str
    rg: str
    cpf: str

    def exibirDados(self):
        print(f"\nNome: {self.nome}\nData de nascimento: {self.dataN}\nRG: {self.rg}\nCPF: {self.cpf}\n")

listaPessoa = []
QTD_PESSOA = 5

for i in range(QTD_PESSOA):
    pessoa1 = Brasileiro(input("Insira seu nome: "),
                         input("Insira sua data de nascimento: "),
                         input("Insira seu RG: "),
                         input("Insira seu CPF: "))
    listaPessoa.append(pessoa1)

arquivo = "dadosPessoa.txt"
with open(arquivo, "a", encoding="utf-8") as dados_pessoais:
    for pessoa1 in listaPessoa:
        dados_pessoais.write(f"{pessoa1.nome} | {pessoa1.dataN} | {pessoa1.rg} | {pessoa1.cpf}")

for pessoa1 in listaPessoa:
    pessoa1.exibirDados()