# CALCULANDO SENO COSSENO E TANGENTE
import emoji
from math import radians,sin,cos,tan
a = float(input('Digite o ângulo que você deseja :'))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))

print('O ângulo de {} tem o SENO de {:.2f}'.format(a,s))
print('O ãngulo de {} tem o COSSENO de {:.2f}'.format(a,c))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(a,t)) 
print('U+1F618')