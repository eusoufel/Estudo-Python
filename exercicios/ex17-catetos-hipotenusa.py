# CATETOS E HIPOTENUSA
# Formula hipotenusa (o ** 2 + a ** 2) ** (1/2)
from math import hypot

o = float(input('Comprimento do cateto oposto : '))
a = float(input('Comprimento do cateto adjacente : '))
h = hypot(o,a)
print('A hipotenusa vai medir {:.2f}'.format(h))