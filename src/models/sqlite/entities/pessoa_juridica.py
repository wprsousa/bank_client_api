from sqlalchemy import Column, BIGINT, String, Float
from src.models.sqlite.settings.base import Base


class PessoaJuridicaTable(Base):
    __tablename__ = "pessoa_juridica"

    id = Column(BIGINT, primary_key=True)
    faturamento = Column(Float)
    idade = Column(BIGINT)
    nome_fantasia = Column(String)
    celular = Column(String)
    email_corporativo = Column(String)
    categoria = Column(String)
    saldo = Column(Float)

    def __repr__(self):
        return (f"<PessoaJuridica(id={self.id}, nome_fantasia={self.nome_fantasia}, celular={self.celular}, "
                f"email_corporativo={self.email_corporativo}, categoria={self.categoria}, saldo={self.saldo})>")
