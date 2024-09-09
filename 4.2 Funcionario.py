import os
from numpy import double
from enum import Enum

os.system("cls || clear")

class Sexo(Enum):
    """Definindo valores de Enum"""
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Setor(Enum):
    FINANCEIRO = "Financeiro"
    RECURSOS_HUMANOS = "Recursos Humanos"
    VENDAS = "Vendas"
    MARKETING = "Marketing"

class Funcionario:
    def __init__(self, id:int, nome:str, idade:int, salario: double, setor:Setor, sexo:Sexo) -> None:
        self.id = id
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.setor = setor
        self.sexo = sexo

    def __str__(self) -> str:
        return (f"ID: {self.id} \nNome: {self.nome} \nIdade: {self.idade} \nSalário: {self.salario} \nSetor: {Setor.FINANCEIRO.value} \nSexo: {Sexo.FEMININO.value}")

funcionario1 = Funcionario("321", "Marta", 22, 5500.0, Setor.FINANCEIRO, Sexo.FEMININO)
print(funcionario1)
