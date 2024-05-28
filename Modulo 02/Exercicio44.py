print('=========DESAFIO44=========')
preco = float(input('qual preço do produto? R$'))
print('''[1] A vista'
      [2] A vista no cartão
      [3] 2x no cartão
      [4] 3x ou mais''')
condicao = int(input('Qual vai ser a forma de pagamento? '))
if condicao == 1:
    desconto = preco * 10 / 100
    novopreco = preco - desconto
    print('Você ganhou R${:.2f} de desconto e o seu novo preço será de R${:.2f}'.format(desconto, novopreco))
elif condicao == 2:
    desconto = preco * 5 / 100
    novopreco = preco - desconto
    print('Você ganhou R${:.2f} de desconto e o seu novo preço será de R${:.2f}'.format(desconto, novopreco))
elif condicao == 3:
    print('Voce nao possui nenhum tipo de desconto')
elif condicao == 4:
    juros = 20 / 100 * preco
    novopreco = preco + juros
    parcela = int(input('Quantas Parcelas? '))
    print('Voce teve um acrescimos na sua compra de R${:.2f} e seu novo preço será R${:.2f}'.format(juros,novopreco))
else:
    print('Opcao invalida de pagamento')