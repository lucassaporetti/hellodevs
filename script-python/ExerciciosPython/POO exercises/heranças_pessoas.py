#  Relação de herança:


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'O {self.nomeclasse} está falando!')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome} está comprando!')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome} está estudando!')


cliente1 = Cliente('Lucas', 30)
print(cliente1.nome, cliente1.idade)
print(f'{cliente1.nome} é um {cliente1.nomeclasse}')
cliente1.falar()
cliente1.comprar()
print()

aluno1 = Aluno('John', 64)
print(aluno1.nome, aluno1.idade)
print(f'{aluno1.nome} é um {aluno1.nomeclasse}')
aluno1.falar()
aluno1.estudar()
print()

p1 = Pessoa('Paul', 80)
p1.falar()

