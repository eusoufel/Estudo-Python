# Dissecando uma variável 

s = input('Digite algo: ')

print('O tipo primitivo desse valor é {} '.format(type(s)))

print('Só tem espaços? {}'.format(s.isspace()))
print('É um número? {}'.format(s.isalnum()))
print('É alfbético? {}'.format(s.isalpha()))
print('É alfanúmerico? {}'.format(s.isalnum()))
print('Está em maiúscula? {}'.format(s.isupper()))
print('Está em minúscula? {}'.format(s.islower()))
print('Está Capitalizada? {}'.format(s.istitle()))