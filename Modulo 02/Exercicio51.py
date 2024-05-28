print('=========DESAFIO51=========')
primeirotermo = int(input('Digite o primeiro termo do PA: '))
razao = int(input('Digite a razâo do PA: '))
decimo = primeirotermo +(10 - 1) * razao
for c in range(primeirotermo, decimo + razao, razao):
    print(c,end=' -> ')
print('ACABOU!!')