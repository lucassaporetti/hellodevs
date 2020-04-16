#  Relação de composição:


class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        print(f'{self.nome} foi apagado!')


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade} e {self.estado} foram apagados!')


cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereco('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
print()
del cliente1
print()

cliente2 = Cliente('Lucas,', 30)
cliente2.insere_endereco('Salvador', 'BA')
print(cliente2.nome)
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
cliente2.lista_enderecos()
print()

cliente3 = Cliente('João', 19)
cliente3.insere_endereco('São Paulo', 'SP')
print(cliente3.nome)
cliente3.lista_enderecos()
print()

print('#' * 50)
