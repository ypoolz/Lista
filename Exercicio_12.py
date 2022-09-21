# Faça um programa que leia um número natural N e calcule a soma abaixo (lembre-se de que tanto as divisões
# quanto o resultado devem ser decimais). Utilize o laço que lhe for mais conveniente.

Number = int(input('Digite um número: '))
soma_total = 0
soma = 0
cont = 1
n = 1
s = 0
while cont <= Number:
    soma = (n / cont)
    soma_total += soma
    cont += 1
    s = soma_total - 1
    print('A soma das divisões é: {:.2f}'.format(s))