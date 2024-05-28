print('=========DESAFIO32=========')
from datetime import date
ano = int(input(('Digite o ano para analisar se ê bissexto: ')))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('O ano digitado {} é bissexto'.format(ano))
else:
    print('O ano digitado {} nao ê bissexto'.format(ano))