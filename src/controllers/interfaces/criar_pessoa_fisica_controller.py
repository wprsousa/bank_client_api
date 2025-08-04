from abc import ABC, abstractmethod


class CriarPessoaFisicaControllerInterface(ABC):
    @abstractmethod
    def criar_pessoa_fisica(self, info_pessoa_fisica: dict) -> dict:
        pass
