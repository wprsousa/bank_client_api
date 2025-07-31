from src.models.sqlite.entities.pessoas_fisicas import PessoaFisicaTable
from src.models.sqlite.interfaces.clientes_repository import (
    ClientesRepositoryInterface,
)


class PessoasFisicasRepository(ClientesRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def criar_pessoa_fisica(
        self,
        renda_mensal: float,
        idade: int,
        nome_completo: str,
        celular: str,
        email: str,
        categoria: str,
        saldo: float,
    ) -> None:
        with self.__db_connection as database:
            try:
                database.session.add(
                    PessoaFisicaTable(
                        renda_mensal=renda_mensal,
                        idade=idade,
                        nome_completo=nome_completo,
                        celular=celular,
                        email=email,
                        categoria=categoria,
                        saldo=saldo,
                    )
                )
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def verificar_saldo(self, nome_completo: str) -> float:
        with self.__db_connection as database:
            try:
                result = (
                    database.session.query(PessoaFisicaTable)
                    .filter_by(nome_completo=nome_completo)
                    .first()
                )
                return result.saldo
            except Exception as exception:
                database.session.rollback()
                raise exception

    def sacar_dinheiro(self, nome_completo, valor_saque):
        limite_saque = 5000

        saldo_atual = self.verificar_saldo(nome_completo)

        if valor_saque <= limite_saque and valor_saque <= saldo_atual:
            saldo_atual -= valor_saque
            return f"Saque de {valor_saque} realizado com sucesso! Saldo atual: {saldo_atual}"
        else:
            return f"Saldo {saldo_atual} insuficiente!"

    def realizar_extrato(self, nome_completo):
        with self.__db_connection as database:
            try:
                result = (
                    database.session.query(PessoaFisicaTable)
                    .filter_by(nome_completo=nome_completo)
                    .first()
                )
                return {
                    "nome_completo": result.nome_completo,
                    "saldo": result.saldo,
                    "categoria": result.categoria,
                }
            except Exception as exception:
                raise exception
