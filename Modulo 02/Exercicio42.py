print('=========DESAFIO42=========')
a = float(input('Digite o primeiro lado do triangulo: '))
b = float(input('Digite o seguhdo lado do triangulo: '))
c = float(input('Digite o terceiro lado do triangulo: '))
if a + b > c and a + c > b and b + c > a:
    print('Os tres lados digitados formam um triangulo')
    if a == b and b == c:
        print('O triangulo é do tipo equilatéro')
    elif a == b or b == c:
        print('O triangulo é do tipo isósceles')
    else:
        print('O triangulo é do tipo escaleno')
else:
    print('Os tres lados digitados nao formam um triangulo')

