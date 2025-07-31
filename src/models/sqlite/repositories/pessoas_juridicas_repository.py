from src.models.sqlite.entities.pessoas_juridicas import PessoaJuricaTable

from src.models.sqlite.interfaces.clientes_repository import ClientesRepositoryInterface


class PessoaJuridicaRepository(ClientesRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def criar_pessoa_juridica(
            self,
            faturamento: float,
            idade: int,
            nome_fantasia: str,
            celular: str,
            email_corporativo: str,
            categoria: str,
            saldo: float,
    ) -> None:
        with self.__db_connection as database:
            try:
                database.session.add(
                    PessoaJuricaTable(
                        faturamento=faturamento,
                        idade=idade,
                        nome_fantasia=nome_fantasia,
                        celular=celular,
                        email_corporativo=email_corporativo,
                        categoria=categoria,
                        saldo=saldo,
                    )
                )
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def verificar_saldo(self, nome_fantasia: str) -> float:
        with self.__db_connection as database:
            try:
                result = (
                    database.session.query(PessoaJuricaTable)
                    .filter_by(nome_fantasia=nome_fantasia)
                    .first()
                )
                return result.saldo
            except Exception as exception:
                database.session.rollback()
                raise exception

    def sacar_dinheiro(self, nome_fantasia, valor_saque):
        limite_saque = 15000

        saldo_atual = self.verificar_saldo(nome_fantasia)

        if valor_saque <= limite_saque and valor_saque <= saldo_atual:
            saldo_atual -= valor_saque
            return f"Saque de {valor_saque} realizado com sucesso! Saldo atual: {saldo_atual}"
        else:
            return f"Saldo {saldo_atual} insuficiente!"

    def realizar_extrato(self, nome_fantasia):
        with self.__db_connection as database:
            try:
                result = (
                    database.session.query(PessoaJuricaTable)
                    .filter_by(nome_fantasia=nome_fantasia)
                    .first()
                )
                return {
                    "nome_fantasia": result.nome_fantasia,
                    "saldo": result.saldo,
                    "categoria": result.categoria,
                }
            except Exception as exception:
                raise exception
