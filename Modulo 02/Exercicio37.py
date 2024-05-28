print('=========DESAFIO37=========')
numero = int(input('Digite um número para fazer a conversão: '))
print('Digite qual a base para converter o número digitado: ')
print('-1 para converter em Binário')
print('-2 para converter em octadécimal')
print('-3 Converter em hexadecimal')
seleciona = int(input(''))
if seleciona == 1:
    binario = bin(numero)
    print(binario)
elif seleciona == 2:
    octal = oct(numero)
    print(octal)
elif seleciona == 3:
    hexa = hex(numero)
    print(hexa)
else:
    print('Número digitado inválido')
