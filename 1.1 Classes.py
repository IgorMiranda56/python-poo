import os

os.system("clear || cls") # Limpar terminal.

class Aluno:
    # nome, idade
    # Construtor.
    def __init__(self, nome: str, idade: int) -> None:
        # Atributos.
        self.nome = nome
        self.idade = idade
    
    def exibir_dados(self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.idade}"

# Instanciar classe.
aluno = Aluno("Marta", 22)

# print(f"Nome:  {aluno.nome}")
# print(f"Idade:  {aluno.idade}")
print(aluno.exibir_dados())