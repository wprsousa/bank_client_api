from decimal import Decimal

from sqlmodel import SQLModel, Field, REAL


class PessoaJuricaTable(SQLModel, table=True):
    """
    Represents a corporate entity ("Pessoa Jurídica") mapped to the corresponding table in the database.

    Attributes:
        id (int): Primary key. Unique identifier for the corporation.
        faturamento (REAL): Revenue or turnover of the company.
        idade (int): Age of the company.
        nome_fantasia (str): Trade name of the company.
        celular (str): Corporate mobile phone number.
        email_corporativo (str): Corporate email address.
        categoria (str): Category or sector of the company.
        saldo (REAL): Current account balance of the company.

    Methods:
        __repr__():
            Returns a formatted string that represents the company for debugging and logging purposes.
    """
    __tablename__ = "pessoa_juridica"

    id: int = Field(primary_key=True)
    faturamento: Decimal = Field(max_digits=5, decimal_places=2)
    idade: int
    nome_fantasia: str
    celular: str
    email_corporativo: str
    categoria: str
    saldo: Decimal = Field(max_digits=5, decimal_places=2)

    def __repr__(self):
        return (
            f"<PessoaJuridica(id={self.id}, nome_fantasia={self.nome_fantasia}, celular={self.celular}, "
            f"email_corporativo={self.email_corporativo}, categoria={self.categoria}, saldo={self.saldo})>"
        )
