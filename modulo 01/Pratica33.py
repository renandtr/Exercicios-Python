print('=========DESAFIO33=========')
l1 = float(input('Digite o primeiro numero: '))
l2 = float(input('Digite o segundo numero: '))
l3 = float(input('Digite o terceiro numero: '))
if l1 > l2 and l2 > l3:
    print(l1)
    print(l3)
elif l2 > l1 and l1 >l3:
   print(l2)
   print(l3)
else:
    print(l3)
    print(l2)