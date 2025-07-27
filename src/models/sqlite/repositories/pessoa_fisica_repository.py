from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from src.models.sqlite.interfaces.cliente_repository import ClienteRepository


class PessoaFisicaRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def criar_cliente(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str,
                      categoria: str, saldo: float) -> None:
        with self.__db_connection as database:
            try:
                cliente = PessoaFisicaTable(renda_mensal=renda_mensal, idade=idade, nome_completo=nome_completo,
                                            celular=celular, email=email, categoria=categoria, saldo=saldo)
                database.session.add(cliente)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
