from sqlmodel import create_engine, Session


class DBConnectionHandler:
    """
        Handles the creation and management of the database connection using SQLModel and SQLAlchemy.

        Attributes:
            __connection_string (str): The connection string that defines the database location.
            __engine: The SQLAlchemy engine instance, created upon connection.
            session: The SQLModel session instance for executing database operations.

        Methods:
            __init__():
                Initializes the handler with the default connection string and sets engine/session to None.

            connect_to_db():
                Creates the SQLAlchemy engine using the connection string.
                Should be called before performing database operations.

            engine (property):
                Returns the internal SQLAlchemy engine instance.

            __enter__():
                Enables use as a context manager. Creates a new session object and returns self.

            __exit__(exc_type, exc_val, exc_tb):
                Ensures proper closing of the session when exiting the context manager scope.
        """

    def __init__(self) -> None:
        self.__connection_string = "sqlite:///storage.db"
        self.__engine = None
        self.session = None

    def connect_to_db(self):
        self.__engine = create_engine(self.__connection_string)

    @property
    def engine(self):
        return self.__engine

    def __enter__(self):
        self.session = Session(self.engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


db_connection_handler = DBConnectionHandler()
"""
A singleton-like instance of DBConnectionHandler to be reused across the application.
"""
