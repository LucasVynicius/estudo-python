# Exemplo de Herança
print("\nExemplo de herança:")
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def anda(self):
        print(f"O animel {self.nome} andou")
        return
    
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        return "Au, au, au..."
    
class Gato(Animal):
    def emitir_som(self):
        return "miau, miau, miau..."
    

caramelo = Cachorro(nome="Chase")
siames = Gato(nome="Baga")

print("\nExemplo de polimorfismo:")
animais = [caramelo, siames]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")

print("\nExemplo de encapsulamento:")
class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo
    
conta = ContaBancaria(saldo=1000)
print(f"Saldo da conta: {conta.consultar_saldo()}")
conta.depositar(valor=500)
print(f"Saldo da conta: {conta.consultar_saldo()}")
conta.sacar(valor=800)
print(f"Saldo da conta: {conta.consultar_saldo()}")

print("\nExemplo de Abstração:")
from abc import ABC, abstractmethod

class Veiculo(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self) -> None:
        pass
    def ligar(self):
        return "Carro ligado, vruuum"
    
    def desligar(self):
        return "Carro desligado"

fusca = Carro()
print(fusca.ligar())
print(fusca.desligar())