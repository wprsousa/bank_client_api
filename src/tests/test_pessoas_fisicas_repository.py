from unittest.mock import MagicMock

import pytest

from src.models.sqlite.repositories.pessoas_fisicas_repository import (
    PessoasFisicasRepository,
)
from src.models.sqlite.entities.pessoas_fisicas import PessoaFisicaTable

data = [
    PessoaFisicaTable(
        id=1,
        renda_mensal=7000.00,
        idade=39,
        nome_completo="Fulano de Tal",
        celular="13999999999",
        email="fulano@gmail.com",
        categoria="Categoria A",
        saldo=12456.98,
    ),
    PessoaFisicaTable(
        id=2,
        renda_mensal=7000.00,
        idade=39,
        nome_completo="Sicrano da Silva",
        celular="13999999999",
        email="fulano@gmail.com",
        categoria="Categoria A",
        saldo=12456.98,
    ),
]


@pytest.fixture
def mock_db_handler():
    mock_session = MagicMock()
    mock_db_handler = MagicMock()
    mock_db_handler.__enter__.return_value.session = mock_session
    return mock_db_handler, mock_session


def test_criar_pessoa_fisica(mock_db_handler):
    mock_db, mock_session = mock_db_handler

    repo = PessoasFisicasRepository(mock_db)
    repo.criar_pessoa_fisica(
        7000.00,
        39,
        "Sicrano da Silva",
        "13981292148",
        "sicrano@gmail.com",
        "Categoria B",
        53000.55,
    )

    args, kwargs = mock_session.add.call_args
    individual = args[0]

    assert isinstance(individual, PessoaFisicaTable)
    assert individual.renda_mensal == 7000.00
    assert individual.idade == 39
    mock_session.commit.assert_called_once()


def test_verificar_saldo(mock_db_handler):
    mock_db, mock_session = mock_db_handler
    mock_query = MagicMock()
    mock_query.filter_by.return_value.first.return_value = data[1]
    mock_session.query.return_value = mock_query

    repo = PessoasFisicasRepository(mock_db)
    response = repo.verificar_saldo("Sicrano da Silva")

    assert response == 12456.98
    assert isinstance(response, float)
    mock_query.filter_by.assert_called_once_with(nome_completo="Sicrano da Silva")


def test_sacar_dinheiro(mock_db_handler):
    mock_db, mock_session = mock_db_handler
    mock_query = MagicMock()
    mock_query.filter_by.return_value.first.return_value = data[1]
    mock_session.query.return_value = mock_query

    repo = PessoasFisicasRepository(mock_db)
    response = repo.sacar_dinheiro("Sicrano da Silva", 1000)

    assert response == "Saque de 1000 realizado com sucesso! Saldo atual: 11456.98"
    assert isinstance(response, str)
    mock_query.filter_by.assert_called_once_with(nome_completo="Sicrano da Silva")


def test_realizar_extrato(mock_db_handler):
    mock_db, mock_session = mock_db_handler
    mock_query = MagicMock()
    mock_query.filter_by.return_value.first.return_value = data[1]
    mock_session.query.return_value = mock_query

    repo = PessoasFisicasRepository(mock_db)
    response = repo.realizar_extrato("Sicrano da Silva")

    assert response == {
        "nome_completo": "Sicrano da Silva",
        "saldo": 12456.98,
        "categoria": "Categoria A",
    }
    assert isinstance(response, dict)
    mock_query.filter_by.assert_called_once_with(nome_completo="Sicrano da Silva")