from pessoa import Pessoa

p1 = Pessoa('Lucas', 30)
p2 = Pessoa('John', 64)

p1.parar_comer()
p1.comer('pizza')
p1.falar('Oi')
p1.parar_falar()
p1.parar_comer()
p1.falar('Python 3')
p1.falar('POO')
p1.parar_falar()
p1.comer('sushi')
p1.comer('chocolate')

print(p1.get_ano_nascimento())

p3 = Pessoa.por_ano_nascimento('Paul', 1942)

print(p1)

print(p3.idade)

print(Pessoa.gera_id())

print(p1.gera_id())
