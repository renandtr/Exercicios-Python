print('=========DESAFIO49=========')
numero = int(input('Digite o número para que possa mostrar a tabuada: '))
for c in range(0, 10+1, 1):
    resultado = numero * c
    print('{} x {} = {}'.format(numero, c, resultado))