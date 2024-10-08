# ALUGUEL DE CARRO calculos


d = int(input('Quantos dias alugados ? '))
k = int(input('Quantos km rodados ? '))

dia = d * 60
km = k * 0.15

print('O valor total a pagar é de R$:{:.2f}'.format(dia + km))