from abc import ABC, abstractmethod


class SacarDinheiroPessoaFisicaControllerInterface(ABC):
    @abstractmethod
    def sacar_dinheiro(self, nome_pessoa_fisica: str, valor_a_sacar: float) -> str:
        pass
