from sqlmodel import select
from sqlalchemy.exc import NoResultFound

from src.models.sqlite.entities.individuals import IndividualsTable


class IndividualsRepository:
    """
    Repository responsible for managing operations related to the `IndividualsTable`
    entity in the SQLite database, using SQLModel and SQLAlchemy.

    Methods:
        __init__(db_connection):
            Initializes the repository with a database connection instance.

        list_individuals() -> list[IndividualsTable]:
            Retrieves all individuals stored in the `IndividualsTable`.
            Returns a list of table instances or an empty list if no records are found.
    """

    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def list_individuals(self) -> list[IndividualsTable]:
        with self.__db_connection as database:
            try:
                statement = select(IndividualsTable)
                result = database.session.exec(statement).all()
                return result
            except NoResultFound:
                return []

    def create_individual(self, individual: IndividualsTable) -> IndividualsTable:
        with self.__db_connection as database:
            try:
                pass
            except:
                pass
