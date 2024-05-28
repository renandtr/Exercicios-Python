print('=========DESAFIO29=========')
velocidade = float(input('Qual velocidade o carro atingiu? '))
if velocidade > 80:
    ve = velocidade - 80
    multa = ve * 7.00
    print('sua velocidade foi {}, voce excedeu o limite de velocidade, sua multa é de R${:.2f}'.format(velocidade,multa))
else:
    print('Voce nao excedeu limite de velocidade')