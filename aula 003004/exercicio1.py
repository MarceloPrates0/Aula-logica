from dataclasses import dataclass
import os
os.system("cls || clear")

@dataclass
class Paciente:
    nome: str
    idade: int

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade}\n\n")

paciente1 = Paciente("Marta", 18)

paciente1.exibir_dados()