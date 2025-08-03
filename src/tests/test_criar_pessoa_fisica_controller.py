import pytest

from src.controllers.criar_pessoa_fisica_controller import CriarPessoaFisicaController


class MockRepository:
    def insere_pessoa_fisica(
            self,
            renda_mensal: float,
            idade: int,
            nome_completo: str,
            celular: str,
            email: str,
            categoria: str,
            saldo: float,
    ) -> None:
        pass


def test_criar_pessoa_fisica_controller():
    repository = MockRepository()
    controller = CriarPessoaFisicaController(repository)
    info_pessoa_fisica = {
        "renda_mensal": 1000,
        "idade": 20,
        "nome_completo": "Wellington Sousa",
        "celular": "11988675309",
        "email": "teste@gmail.com",
        "categoria": "Categoria A",
        "saldo": 10000.00,
    }

    response = controller.criar_pessoa_fisica(info_pessoa_fisica)

    assert response["data"]["tipo"] == "Pessoa Física"
    assert response["data"]["quantidade"] == 1
    assert response["data"]["atributos"] == info_pessoa_fisica


def test_criar_pessoa_fisica_controller_invalid_nome_completo():
    info_pessoa_fisica = {
        "renda_mensal": 1000,
        "nome_completo": "Wellington123",
        "celular": "11988675309",
        "email": "teste@gmail.com",
        "categoria": "Categoria A",
        "saldo": 10000.00,
    }

    controller = CriarPessoaFisicaController(MockRepository())

    with pytest.raises(Exception):
        controller.criar_pessoa_fisica(info_pessoa_fisica)



def test_criar_pessoa_fisica_controller_invalid_rensa_mensal():
    info_pessoa_fisica = {
        "renda_mensal": "mil",
        "nome_completo": "Wellington",
        "celular": "11988675309",
        "email": "teste@gmail.com",
        "categoria": "Categoria A",
        "saldo": 10000.00,
    }

    controller = CriarPessoaFisicaController(MockRepository())

    with pytest.raises(Exception):
        controller.criar_pessoa_fisica(info_pessoa_fisica)


def test_criar_pessoa_fisica_controller_invalid_saldo():
    info_pessoa_fisica = {
        "renda_mensal": 1000,
        "nome_completo": "Wellington",
        "celular": "11988675309",
        "email": "teste@gmail.com",
        "categoria": "Categoria A",
        "saldo": "dezmil",
    }

    controller = CriarPessoaFisicaController(MockRepository())

    with pytest.raises(Exception):
        controller.criar_pessoa_fisica(info_pessoa_fisica)