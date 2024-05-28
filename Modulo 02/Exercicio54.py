from datetime import date
print('=========DESAFIO54==========')
anoatual = date.today().year
totmaior = 0
totmenor = 0
for c in range(0, 7, 1):
    nascimento = int(input('Digite o ano da {} nascimento: '.format(c)))
    idade = anoatual - nascimento
    if idade > 18:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1
print('O total de pessoas  maior de idade é {}'.format(totmaior))
print('O total de pessoas menor de idade é {}'.format(totmenor))