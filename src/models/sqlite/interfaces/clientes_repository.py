from abc import ABC, abstractmethod


@abstractmethod
class ClientesRepositoryInterface(ABC):
    def sacar_dinheiro(self, individual, amount):
        pass

    def realizar_extrato(self, individual):
        pass
