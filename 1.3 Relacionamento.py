import os

os.system("clear || cls") # Limpar terminal.

class Endereco:
    def __init__(self, logradouro: str, numero: int) -> None:
        self.logradouro = logradouro
        self.numero = numero

    def exibir_endereco(self) -> str:
        return f"\nLogradouro: {self.logradouro} \nNúmero: {self.numero}"
    
class Aluno:
    # Construtor.
    def __init__(self, nome: str, idade: int, endereco: Endereco) -> None:
        # Atributos.
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
    
    def exibir_dados(self) -> str:
        return f"Aluno: \nNome: {self.nome} \nIdade: {self.idade} \n\nEndereço: {self.endereco.exibir_endereco()}"

# Instanciar classe.
aluno1 = Aluno("Marta", 22, Endereco("Rua A", 202))

print(aluno1.exibir_dados())