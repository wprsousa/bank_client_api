from src.models.sqlite.repositories.pessoas_fisicas_repository import (
    PessoasFisicasRepository,
)

from src.utils.validador import Validator
from src.controllers.interfaces.criar_pessoa_fisica_controller import (
    CriarPessoaFisicaControllerInterface,
)


class CriarPessoaFisicaController(CriarPessoaFisicaControllerInterface):
    def __init__(self, pessoa_fisica_repository: PessoasFisicasRepository):
        self.__pessoa_fisica_repository = pessoa_fisica_repository

    def criar_pessoa_fisica(self, info_pessoa_fisica: dict) -> dict:
        renda_mensal: float = info_pessoa_fisica["renda_mensal"]
        idade: int = info_pessoa_fisica["idade"]
        nome_completo: str = info_pessoa_fisica["nome_completo"]
        celular: str = info_pessoa_fisica["celular"]
        email: str = info_pessoa_fisica["email"]
        categoria: str = info_pessoa_fisica["categoria"]
        saldo: float = info_pessoa_fisica["saldo"]

        Validator.validar_nome_completo(nome_completo)
        Validator.validar_valor_positivo(renda_mensal)
        self.__insere_pessoa_fisica(
            renda_mensal, idade, nome_completo, celular, email, categoria, saldo
        )
        resposta_formatada = self.__formata_resposta(info_pessoa_fisica)
        return resposta_formatada

    def __insere_pessoa_fisica(
        self,
        renda_mensal: float,
        idade: int,
        nome_completo: str,
        celular: str,
        email: str,
        categoria: str,
        saldo: float,
    ) -> None:
        self.__pessoa_fisica_repository.insere_pessoa_fisica(
            renda_mensal, idade, nome_completo, celular, email, categoria, saldo
        )

    @staticmethod
    def __formata_resposta(info_pessoa_fisica: dict) -> dict:
        return {
            "data": {
                "tipo": "Pessoa Física",
                "quantidade": 1,
                "atributos": info_pessoa_fisica,
            }
        }
