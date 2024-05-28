print('=========DESAFIO34=========')
salario = float(input('Qual salário do funcionário? '))
if salario > 1250.00:
    novosalario = (salario * 0.10) + salario
    print('O salário do funcionário é R${:.2f} e com aumento de 10% fica R${:.2f}'.format(salario,novosalario))
else:
    novosalario = (salario * 0.15) + salario
    print('O salário do funcionário é R${:.2f} e com aumento de 15% fica R${:.2f}'.format(salario,novosalario))