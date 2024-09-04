from abc import ABC, abstractmethod
import os

os.system("clear || cls") # Limpar terminal.

# Criando sua própria exceçâo.
class SaldoInsuficienteError(Exception):
    pass
class ValorNegativoError(Exception):
    pass
 
class Conta:
    def __init__(self, numero_conta: int, agencia: int) -> None:
        self.numero_conta = numero_conta
        self.agencia = agencia
        self._saldo = 0 # _ Atributo protegido.

    @property
    def saldo(self):
        return self._saldo

    def sacar(self, valor):
        # try - except
        try:
            self.__verificar_sacar(valor)
        except SaldoInsuficienteError as error:
            return f"Erro: {error}"
        self._saldo -= valor
        return self._saldo

    #def __verificar_sacar(self, valor): # __ Método privado.
    #    if valor > self.saldo:
    #        raise SaldoInsuficienteError(f"Saldo insuficiente.") # Lançando um erro.

    def depositar(self, valor):
        try:
            self.__verificar_depositar(valor)
        except ValorNegativoError as erro:
            return f"Erro: {erro}"
        
        self._saldo += valor
        return self._saldo
    
    def __verificar_depositar(self, valor):
        if valor < 0:
            raise ValorNegativoError("Nâo é possível depositar valor negativo.")

class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass
        
class Endereco:
    def __init__(self, logradouro: str, numero: int, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade

    def exibir_endereco(self) -> str:
        return f"\nLogradouro: {self.logradouro} \nNúmero: {self.numero} \nCidade: {self.cidade}"
    
class Funcionario(ABC):
    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco) -> None:
        self.nome = nome
        self.email = email
        self.salario = salario
        self.endereco = endereco
    
    @abstractmethod
    def salario_final(self) -> float:
        pass    

class Motoboy(Funcionario):
    def __init__(self, nome: str, email: str, salario: float, cnh: str, endereco: Endereco) -> None:
        super().__init__(nome, email, salario, endereco)
        self.cnh = cnh
    def salario_final(self) -> float: 
        return 1000
    def exibir_dados(self) -> str:
        return f"Nome: {self.nome} \nE-mail: {self.email} \nSalário: {self.salario} \nCnh: {self.cnh} \nEndereco: {self.endereco.exibir_endereco()}"
    
class Gerente(Funcionario):
    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco) -> None:
        super().__init__(nome, email, salario, endereco)
    def salario_final(self) -> float: 
        return 5000
    def exibir_dados(self) -> str:
        return f"Nome: {self.nome} \nE-mail: {self.email} \nSalário: {self.salario} \nEndereco: {self.endereco.exibir_endereco()}"

# Instanciar classes.
conta_corrente = ContaCorrente(222, 333)
#conta_poupanca = ContaPoupanca(444, 555)

motoboy1 = Motoboy("Marta", "@gmail", 1000, "789", Endereco("Rua A", "202", "Salvador"))
print(motoboy1.exibir_dados())
print(motoboy1.salario_final())

print(conta_corrente.saldo)
#print(conta_corrente.sacar(200))
#print(conta_corrente.saldo)
print(conta_corrente.depositar(-200))


gerente1 = Gerente("José", "@hotmail", 5000, Endereco("Rua B", "784", "Rio de Janeiro"))
print(gerente1.exibir_dados())
print(gerente1.salario_final())

print(conta_corrente.saldo)
#print(conta_corrente.sacar(200))
#print(conta_corrente.saldo)
print(conta_corrente.depositar(-200))
