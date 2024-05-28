print('=========DESAFIO43=========')
peso = float(input('digite o seu peso: (Kg)'))
altura = float(input('Digte a sua altura: '))
imc = peso/(altura * altura)
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Voce está no peso ideal')
elif imc >= 25 and imc < 30:
    print('Vocę está acima do peso')
elif imc >= 30 and imc < 40:
    print('Você esta obeso')
else:
    print('voce esta com obesidade morbita')