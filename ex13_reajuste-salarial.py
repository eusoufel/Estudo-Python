# CAUCULANDO O REAJUSTE DE SALARIO


s = float(input('Qual é o salário do Funcionario ? R$:'))

r = s / 100 * 15

print('Um funcionário que ganhava R$:{:.2f}, com 15% de aumento, passa a receber R$:{:.2f}'.format(s, s + r))