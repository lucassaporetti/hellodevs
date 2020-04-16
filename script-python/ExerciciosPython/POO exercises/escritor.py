#  Relação de associação:


class Escritor:
    def __init__(self, nome):
        self.__nome = nome  # setter
        self.__ferramenta = None

    @property  # getter
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('A caneta está escrevendo...')


class Maquina_de_escrever:
    def escrever(self):
        print('A máquina está escrevendo...')


escritor = Escritor('Lucas')
print(escritor.nome)
caneta = Caneta('Bic')
print(caneta.marca)
maquina = Maquina_de_escrever()
maquina.escrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()

