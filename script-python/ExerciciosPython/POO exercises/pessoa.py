from random import randint


class Pessoa:

    from datetime import date

    ano_atual = date.today().year

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def __str__(self):
        return f'Nome: {self.nome} Idade: {self.idade} Comendo: {self.comendo} Falando: {self.falando}'

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo!')
            return
        if self.falando:
            print(f'{self.nome} não pode comer enquanto fala.')
            return
        else:
            print(f'{self.nome} está comendo {alimento}')
            self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não estava comendo nada.')
            return
        else:
            print(f'{self.nome} parou de comer.')
            self.comendo = False

    def falar(self, assunto):
        if self.falando:
            print(f'{self.nome} já está falando!')
            return
        if self.comendo:
            print(f'{self.nome} não pode falar enquanto come.')
            return
        else:
            print(f'{self.nome} está falando sobre {assunto}')
            self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não estava falando nada.')
            return
        else:
            print(f'{self.nome} parou de falar.')
            self.falando = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand

