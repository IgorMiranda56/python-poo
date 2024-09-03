from abc import ABC, abstractmethod
import os

os.system("clear || cls") # Limpar terminal.

class Endereco:
    def __init__(self, logradouro: str, numero: int, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    def exibir_endereco(self) -> str:
        return f"\nLogradouro: {self.logradouro} \nNúmero: {self.numero} \nComplemento: {self.complemento} \nCEP: {self.cep} \nCidade: {self.cidade}"
    
class Funcionario(ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
    
    @abstractmethod
    def salario_final(self) -> float:
        pass    

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crea: str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crea = crea
    def salario_final(self) -> float: 
        return 2500
    def exibir_dados(self) -> str:
        return (f"\nNome: {self.nome} \nTelefone: {self.telefone} \nEmail: {self.email} \nCrea: {self.crea} \nEndereço: {self.endereco.exibir_endereco()}")


class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crm: str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crm = crm
    def salario_final(self) -> float: 
        return 5000
    def exibir_dados(self) -> str:
        return (f"\nNome: {self.nome} \nTelefone: {self.telefone} \nEmail: {self.email} \nCrm: {self.crm} \nEndereço: {self.endereco.exibir_endereco()}")

# Instanciar classes.
engenheiro1 = Engenheiro("Marta", "71 9", "@gmail", Endereco("Rua A", 23, "Bloco A", "789", "Salvador"), "2585")
print(engenheiro1.exibir_dados())
print(engenheiro1.salario_final())

medico1 = Medico("José", "11 9", "@hotmail", Endereco("Rua B", 78, "Bloco B", "1478", "São Paulo"), "694")
print(medico1.exibir_dados())
print(medico1.salario_final())
