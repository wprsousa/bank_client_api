import re


class Validator:
    @staticmethod
    def validar_nome_completo(nome_completo: str) -> None:
        if re.search(r"[^a-zA-Z\s]", nome_completo):
            raise ValueError("Nome completo inválido")

    @staticmethod
    def validar_valor_positivo(valor: float) -> None:
        if valor <= 0:
            raise ValueError("Valor deve ser maior que zero")

        if re.search(r"[^0-9]", str(valor).replace(".", "")):
            raise ValueError("Valor digitado está incorreto")
