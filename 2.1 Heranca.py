from abc import ABC, abstractmethod
import os

os.system("clear || cls") # Limpar terminal.

class Funcionario(ABC):
    # Construtor.
    def __init__(self, nome: str, idade: int, salario: float) -> None:
        self.nome = nome
        self.idade = idade
        self.salario = salario

    @abstractmethod
    def calcular_salario(self) -> float:
        pass    

class Gerente(Funcionario):
    def calcular_salario(self) -> float:
        # Acréscimo de 20%
        BONFICACAO = 1.2 
        salario_final = self.salario * BONFICACAO
        return salario_final

class Motoboy(Funcionario):
    def __init__(self, nome: str, idade: int, salario: float, cnh: str) -> None:
        super().__init__(nome, idade, salario)
        self.cnh = cnh
    def calcular_salario(self) -> float:
        # Acréscimo de 10%
        BONIFICACAO = 1.1
        salario_final = self.salario * BONIFICACAO
        return salario_final

# Instanciar classes.

gerente1 = Gerente("Marta", 22, 1000)
print(f"Nome: {gerente1.nome}")
print(f"Idade: {gerente1.idade}")
print(f"Salário: {gerente1.calcular_salario()}")

motoboy1 = Motoboy("José", 33, 1000, "754158")
print(f"\nNome: {motoboy1.nome}")
print(f"Idade: {motoboy1.idade}")
print(f"Salário: {motoboy1.calcular_salario()}")
print(f"Cnh: {motoboy1.cnh}")