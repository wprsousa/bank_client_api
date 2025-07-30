from decimal import Decimal
from sqlmodel import SQLModel, Field


class IndividualsTable(SQLModel, table=True):
    """
    Represents an individual (physical person) entity mapped to the 'pessoa_fisica' table in the database.

    Attributes:
        id (int): Primary key. Unique identifier for the individual.
        renda_mensal (Decimal): Monthly income of the individual.
        idade (int): Age of the individual.
        nome_completo (str): Full name of the individual.
        celular (str): Mobile phone number.
        email (str): Email address.
        categoria (str): Category or classification of the individual.
        saldo (Decimal): Account balance related to the individual.

    Methods:
        __repr__():
            Returns a string representation of the individual for easier debugging and logging.
    """

    __tablename__ = "pessoa_fisica"

    id: int = Field(primary_key=True)
    renda_mensal: Decimal = Field(max_digits=5, decimal_places=2)
    idade: int
    nome_completo: str
    celular: str
    email: str
    categoria: str
    saldo: Decimal = Field(max_digits=5, decimal_places=2)

    def __repr__(self):
        return (
            f"<PessoaFisica(id={self.id}, nome_completo={self.nome_completo}, celular={self.celular}, "
            f"email={self.email}, categoria={self.categoria}, saldo={self.saldo})>"
        )
