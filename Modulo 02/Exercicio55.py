print('========DESAFIO55========')
maior = 0
menor = 0
for c in range(0, 5, 1):
    peso = int(input('Quantos kilos a {} pessoa tem?'.format(c)))
    if c == 1:
        maior = c
        menor = c
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {}Kg'.format(maior))
print('O menor peso lido foi {}Kg'.format(menor))
