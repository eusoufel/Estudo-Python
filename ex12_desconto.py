# CALCULANDO O DESCONTRO DO PRODUTO

p = float(input('Qual é o preço do produto ? R$:'))
d = p / 100  * 5
print('O produto custa R$:{}, na promoção com desconto de 5% vai custar R$:{:.2f}'.format(p,p - d ))