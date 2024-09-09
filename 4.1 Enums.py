from enum import Enum

class Sexo(Enum):
    """Definindo valores de Enum"""
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Pessoa:
    def __init__(self, nome:str, idade:int, sexo: Sexo) -> None:
        """Construtor"""
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def __str__(self) -> str:
        """Equivalente ao toString() do Java"""
        return (f"\nNome: {self.nome}" 
                f"\nIdade: {self.idade}" 
                f"\nSexo: {self.sexo.value}")
    
pessoa1 = Pessoa("Marta", 22, Sexo.FEMININO)
print(pessoa1)