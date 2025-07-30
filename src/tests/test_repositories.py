import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.individuals_repository import IndividualsRepository

db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="interacao com banco de dados")
def test_list_individuals():
    repo = IndividualsRepository(db_connection_handler)
    response = repo.list_individuals()
    print()
    print(response)
