from math import cos, sin, tan, radians
print('Vamos calcular o cosseno, o seno e a tangente de um ângulo?\n')
a = int(input('Informe o ângulo a ser calculado: '))
c = cos(radians(a))
s = sin(radians(a))
t = tan(radians(a))
print('\nO cosseno do ângulo de {}º equivale a {:.2f};\n'
      'o Seno do ângulo de {}º equivale a {:.2f};\n'
      'e a tangente do ângulo de {}° equivale a {:.2f}.'.format(a, c, a, s, a, t))
