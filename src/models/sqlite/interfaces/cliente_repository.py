from abc import ABC, abstractmethod


class ClienteRepository(ABC):
    @abstractmethod
    def sacar_dinheiro(self, pessoa, valor):
        pass

    @abstractmethod
    def realizar_extrato(self, pessoa):
        pass
