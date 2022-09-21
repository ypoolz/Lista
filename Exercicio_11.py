# Faça um programa que calcule e imprima o resultado da soma abaixo (lembre-se de que tanto as divisões
# quanto o resultado devem ser decimais). Utilize o laço que lhe for mais conveniente.

soma_total = 0
soma = 0
cont = 2
n = 1
s = 0
while cont <= 20:
    soma = (n / cont)
    soma_total += soma
    cont += 1
    s = soma_total + 1
    print('A soma das divisões é: {:.2f}'.format(s))

