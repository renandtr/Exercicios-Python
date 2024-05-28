print('=========DESAFIO48=========')
quantidade = 0
soma = 0
for c in range(1, 500+1, 1):
    if c % 2 == 1 and c % 3 == 0:
        quantidade +=1
        soma += c
print('A soma de todos os {} valores é {}'.format(quantidade, soma))
