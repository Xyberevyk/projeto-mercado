class Pessoas:
    def __init__(self, nome: str, idade: int, cpf: str):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf


class Funcionario(Pessoas):
    def __init__(self, ):
