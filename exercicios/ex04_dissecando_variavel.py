# Dissecando uma variável 

s = input('Digite algo? ')

print('O tipo primitivo desse valor é {}'.format(type(s)))
print('Só tem espaços? {}'.format(s.isspace()))
print('É um número? {}'.format(s.isnumeric()))
print('É alfabético? {}'.format(s.isalpha()))
print('É alfanumérico? {}'.format(s.isalnum()))
print('Está em maiúsculo? {}'.format(s.isupper()))
print('Está em minúsculo? {}'.format(s.islower()))
print('Está capitalizada? {}' .format(s.istitle()))