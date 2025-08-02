import re

from src.models.sqlite.repositories.pessoas_fisicas_repository import PessoasFisicasRepository
from src.utils.validador import Validator


class SacarDinheiroPessoaFisicaController:
    def __init__(self, pessoa_fisica_repository: PessoasFisicasRepository) -> None:
        self.__pessoa_fisica_repository = pessoa_fisica_repository

    def sacar_dinheiro(self, nome_pessoa_fisica: str, valor_a_sacar: float) -> str:
        Validator.validar_nome_completo(nome_pessoa_fisica)
        Validator.validar_valor_positivo(valor_a_sacar)
        mensagem = self.__pessoa_fisica_repository.sacar_dinheiro(nome_pessoa_fisica, valor_a_sacar)
        return mensagem

    @staticmethod
    def __valida_nome_completo(nome_completo) -> None:
        nome_nao_valido = re.compile(r"[^a-zA-Z]")

        if nome_nao_valido.search(nome_completo):
            raise Exception("Nome completo inválido")

    @staticmethod
    def __valida_valor_a_sacar(valor_a_sacar: float) -> None:
        valor_nao_valido = re.compile(r"[^0-9]")
        valor_a_sacar_str = str(valor_a_sacar)

        if valor_nao_valido.search(valor_a_sacar_str.replace(".", "")):
            raise ValueError("Valor digitado está incorreto")
