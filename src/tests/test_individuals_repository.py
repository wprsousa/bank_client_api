from unittest.mock import MagicMock

from sqlalchemy.exc import NoResultFound

from src.models.sqlite.repositories.individuals_repository import IndividualsRepository
from src.models.sqlite.entities.individuals import IndividualsTable

data = [IndividualsTable(id=1, renda_mensal=7000.00, idade=39, nome_completo="Fulano de Tal", celular="13999999999",
                         email="fulano@gmail.com", categoria="Categoria A", saldo=12456.98),
        IndividualsTable(id=2, renda_mensal=7000.00, idade=39, nome_completo="Fulano da Silva", celular="13999999999",
                         email="fulano@gmail.com", categoria="Categoria A", saldo=12456.98)]


def test_list_individuals():
    mock_session = MagicMock()
    mock_session.exec.return_value.all.return_value = data

    mock_db_handler = MagicMock()
    mock_db_handler.__enter__.return_value.session = mock_session

    repo = IndividualsRepository(mock_db_handler)
    response = repo.list_individuals()

    assert response == data
    assert isinstance(response, list)
    assert response[0].id == 1
    assert response[1].id == 2
    assert len(response) == 2


def test_list_individuals_with_no_result():
    mock_session = MagicMock()
    mock_session.exec.return_value.all.side_effect = NoResultFound

    mock_db_handler = MagicMock()
    mock_db_handler.__enter__.return_value.session = mock_session

    repo = IndividualsRepository(mock_db_handler)
    response = repo.list_individuals()

    assert response == []
