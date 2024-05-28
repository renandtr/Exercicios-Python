print('=========DESAFIO50=========')
soma = 0
contador = 0
for c in range(0, 6, 1):
    numero = float(input('Digite um número: '))
    if numero % 2 == 0:
        contador = contador + 1
        soma = soma + numero
print('Voce informou {} numeros pares. A soma dos valores pares sao {}'.format(contador,soma))

