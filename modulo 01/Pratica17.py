from math import sqrt
print('=========DESAFIO17=========')
co = float(input(print('Digite o Valor do Cateto Oposto: ')))
ca = float(input(print('Digite o Valor do Cateto Adjascente: ')))
hip = (co**2) + (ca**2)
resultado = sqrt(hip)
print('A hipotenusa vai medir {:.2f}'.format(resultado))
