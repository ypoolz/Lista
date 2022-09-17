# Faça um programa que peça um número inteiro, verifique se é par ou ímpar e mostre a mensagem “O número
# X é par”, quando o número for par ou mostre a mensagem “O número X é ímpar”, quando o número entrado for
# ímpar. O número X mostrado na mensagem é o número que foi entrado. Em seguida o programa pede um novo
# número e repetirá este processo até que se entre o número 0 (zero), quando encerrará o programa. Use o laço
# WHILE.

loop_number = 'number'

while True:
    print('=======LOOPING NUMBER========')
    number = int(input('Digite um número inteiro: '))

    if number == 0:
        print('Programa Encerrado')
        break

    if number % 2 == 0:
        print('Par')

    else:
        print('Ímpar')
