import pytest

from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoa_fisica_repository import PessoaFisicaRepository

db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="interação com o banco")
def test_pessoa_fisica_criar_cliente():
    renda_mensal = 7000.00
    idade = 39
    nome_completo = "Fulano de Tal"
    celular = "11999999999"
    email = "fulanodetal@gmail.com"
    categoria = "Categoria A"
    saldo = 12000.00

    repo = PessoaFisicaRepository(db_connection_handler)
    repo.criar_cliente(renda_mensal, idade, nome_completo, celular, email, categoria, saldo)
