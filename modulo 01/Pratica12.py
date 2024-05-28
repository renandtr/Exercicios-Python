print('=========DESAFIO12=========')
preco = float(input('Qual o preço desse Produto? '))
desconto = preco * 5/100
np = preco - desconto
print('O seu desconto será de {:.2f}R$'.format(desconto))
print('O Valor Final do Produto com o Desconto Aplicado {:.2f}R$'.format(np))

