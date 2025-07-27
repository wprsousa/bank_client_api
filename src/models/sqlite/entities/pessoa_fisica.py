from sqlalchemy import Column, String, BIGINT, REAL
from src.models.sqlite.settings.base import Base


class PessoaFisicaTable(Base):
    __tablename__ = "pessoa_fisica"

    id = Column(BIGINT, primary_key=True)
    renda_mensal = Column(REAL)
    idade = Column(BIGINT)
    nome_completo = Column(String)
    celular = Column(String)
    email = Column(String)
    categoria = Column(String)
    saldo = Column(REAL)

    def __repr__(self):
        return (f"<PessoaFisica(id={self.id}, nome_completo={self.nome_completo}, celular={self.celular}, "
                f"email={self.email}, categoria={self.categoria}, saldo={self.saldo})>")
