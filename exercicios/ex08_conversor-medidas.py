# CONVERTER MEDIDAS MÉTRICAS EM TODAS POSSIBILIDADES


m = float(input('Uma distância em metros :'))

print('{}km'.format(m / 1000))
print('{}hm'.format(m / 100))
print('{}dam'.format(m / 10))
print('{:.0f}dm'.format(m * 10))
print('{:.0f}cm'.format(m * 100))
print('{:.0f}mm'.format(m * 1000))