# CALCULANDO A QUANTIDADE DE TINTA PARA PINTAR PAREDE


l = float(input('Largura da parede :'))
a = float(input('Altura da parede :'))

print('Sua parede tem a dimensão de {} x {} e sua área é de {}m²'.format(l,a,l*a))
print('Para pintar essa parede, você precisará de {}l de tinta'.format((l*a) / 2))