from datetime import date
print('=========DESAFIO41=========')
nascimento = int(input('Qual a data de nascimento do atleta? '))
ano = date.today().year
idade = ano - nascimento
print(idade)
if idade < 9:
    print('MIRIM')
elif idade < 14:
    print('INFANTIL')
elif idade < 19:
    print('JUNIOR')
elif idade >= 19 and idade <= 20:
    print('SENIOR')
else:
    print('MASTER')
