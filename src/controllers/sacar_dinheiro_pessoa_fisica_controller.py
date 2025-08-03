from src.models.sqlite.repositories.pessoas_fisicas_repository import (
    PessoasFisicasRepository,
)
from src.utils.validador import Validator


class SacarDinheiroPessoaFisicaController:
    def __init__(self, pessoa_fisica_repository: PessoasFisicasRepository) -> None:
        self.__pessoa_fisica_repository = pessoa_fisica_repository

    def sacar_dinheiro(self, nome_pessoa_fisica: str, valor_a_sacar: float) -> str:
        Validator.validar_nome_completo(nome_pessoa_fisica)
        Validator.validar_valor_positivo(valor_a_sacar)
        mensagem = self.__pessoa_fisica_repository.sacar_dinheiro(
            nome_pessoa_fisica, valor_a_sacar
        )
        return mensagem
