print('=========DESAFIO40=========')
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno:'))
media = (nota1 + nota2) / 2
if media <= 4:
    print('A  média do aluno foi {:.2f} e está reprovado'.format(media))
elif media >= 5 and media < 6.9:
    print('A  média do aluno foi {:.2f} e está de reposição final'.format(media))
else:
    print('A  média do aluno foi {:.2f} e está aprovado'.format(media))
