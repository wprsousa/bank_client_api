import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pessoas_fisicas_repository import (
    ClientesRepository,
)

db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="interacao com banco de dados")
def test_list_individuals():
    repo = ClientesRepository(db_connection_handler)
    response = repo.list_individuals()
    print()
    print(response)


@pytest.mark.skip(reason="interacao com banco de dados")
def test_create_individual():
    repo = ClientesRepository(db_connection_handler)
    repo.criar_pessoa_fisica(
        7000.00,
        39,
        "Sicrano da Silva",
        "13981292148",
        "sicrano@gmail.com",
        "Categoria B",
        53000.55,
    )
