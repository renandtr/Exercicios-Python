from datetime import date
print('=========DESAFIO39=========')
nascimento = int(input('Digite o ano de nascimento: '))
ano = date.today().year
idade = ano - nascimento
resta = 18 - idade
if idade < 18:
    print('falta {} ano(s) para se alistar no serviço mílitar'.format(resta))
elif idade == 18:
    print('Ta na hora de se alistar')
else:
    print('ja passou {} anos do seu alistamento'.format(abs(resta)))
