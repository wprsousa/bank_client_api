from unittest.mock import MagicMock
import pytest

from src.models.sqlite.entities.pessoas_juridicas import PessoaJuricaTable
from src.models.sqlite.repositories.pessoas_juridicas_repository import PessoaJuridicaRepository

data = [
    PessoaJuricaTable(
        id=1,
        faturamento=180000.00,
        idade=50,
        nome_fantasia="Empresa A",
        celular="11999999999",
        email_corporativo="contato@empresaa.com.br",
        categoria="Categoria A",
        saldo=100000.00
    ),
    PessoaJuricaTable(
        id=2,
        faturamento=70000.00,
        idade=78,
        nome_fantasia="Empresa B",
        celular="11999999999",
        email_corporativo="contato@empresab.com.br",
        categoria="Categoria B",
        saldo=500000.00
    )
]


@pytest.fixture
def mock_db_handler():
    mock_session = MagicMock()
    mock_db_handler = MagicMock()
    mock_db_handler.__enter__.return_value.session = mock_session
    return mock_db_handler, mock_session


def test_criar_pessoa_juridica(mock_db_handler):
    mock_db, mock_session = mock_db_handler
    mock_query = MagicMock()
    mock_query.filter_by.return_value.first.return_value = data[1]
    mock_session.query.return_value = mock_query

    repo = PessoaJuridicaRepository(mock_db)
    repo.criar_pessoa_juridica(
        faturamento=70000.00,
        idade=78,
        nome_fantasia="Empresa B",
        celular="11999999999",
        email_corporativo="contato@empresab.com.br",
        categoria="Categoria B",
        saldo=500000.00
    )

    args, kwargs = mock_session.add.call_args
    individual = args[0]

    assert isinstance(individual, PessoaJuricaTable)
    assert individual.faturamento == 70000.00
    assert individual.idade == 78
    mock_session.commit.assert_called_once()


def test_verificar_saldo(mock_db_handler):
    mock_db, mock_session = mock_db_handler
    mock_query = MagicMock()
    mock_query.filter_by.return_value.first.return_value = data[1]
    mock_session.query.return_value = mock_query

    repo = PessoaJuridicaRepository(mock_db)
    response = repo.verificar_saldo("Empresa B")
    assert response == 500000.00
    assert isinstance(response, float)
    mock_query.filter_by.assert_called_once_with(nome_fantasia="Empresa B")


def test_sacar_dinheiro(mock_db_handler):
    mock_db, mock_session = mock_db_handler
    mock_query = MagicMock()
    mock_query.filter_by.return_value.first.return_value = data[1]
    mock_session.query.return_value = mock_query

    repo = PessoaJuridicaRepository(mock_db)
    response = repo.sacar_dinheiro("Empresa B", 1000)

    assert response == "Saque de 1000 realizado com sucesso! Saldo atual: 499000.0"
    assert isinstance(response, str)
    mock_query.filter_by.assert_called_once_with(nome_fantasia="Empresa B")


def test_realizar_extrato(mock_db_handler):
    mock_db, mock_session = mock_db_handler
    mock_query = MagicMock()
    mock_query.filter_by.return_value.first.return_value = data[1]
    mock_session.query.return_value = mock_query

    repo = PessoaJuridicaRepository(mock_db)
    response = repo.realizar_extrato("Empresa B")

    assert response == {
        "nome_fantasia": "Empresa B",
        "saldo": 500000.0,
        "categoria": "Categoria B"
    }
    assert isinstance(response, dict)
    mock_query.filter_by.assert_called_once_with(nome_fantasia="Empresa B")
