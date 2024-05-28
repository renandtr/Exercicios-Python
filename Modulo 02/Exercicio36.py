from time import sleep
print('=========DESAFIO36=========')
valordacasa = float(input('Qual valor da casa que o comprador quer financiar? R$'))
salario = float(input('Qual  aalario do comprador? R$'))
anos = float(input('Quantos anos o comprador vai pagar? '))
print('Processando.........')
sleep(3)
parcelas = anos * 12
vp = valordacasa / parcelas
autorizar = 30*(salario/100)
print('Os valores das prestações que o comprador irá pagarR${:.2f}'.format(vp))
if parcelas >= autorizar:
    print('Negado, infelizmente vocę nao pode financiar a casa')
else:
    print('Aprovado, voce pode financiar a casa')
