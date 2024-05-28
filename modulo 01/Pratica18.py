import math
print('=========DESAFIO18=========')
angulo = float(input(print('Digite um valor:')))
sen = math.sin(math.radians(angulo))
coss = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print('O Valor do seno de {} é igual a {:.2f}'.format(angulo,sen))
print('O valor do cosseno de {} é igual a {:.2f}'.format(angulo,coss))
print('O Valor da tangente de {} é igual a {:.2f}'.format(angulo,tang))
