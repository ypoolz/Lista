# Leia um valor inteiro N. Este valor será a quantidade de valores que serão lidos em seguida do usuário.
# Para cada valor lido, mostre uma mensagem em português dizendo se este valor lido é par (PAR), ímpar
# (ÍMPAR), positivo (POSITIVO) ou negativo (NEGATIVO). No caso do valor ser igual a zero (0), seu programa
# deverá imprimir apenas NULO. Utilize o laço DO-WHILE.

main_title = 'title'
loop_number = 'number'
count = 0

while True:
    title = print('=======LOOPING NUMBER========')
    number = int(input('Digite um número inteiro: '))
    count += 1

    if number == 0:
        print('Nulo')
        continue

    if number % 2 == 0:
        print('Par')
        if number > 0:
            print('Positivo')
            continue
        else:
            print('Negativo')
            continue
    else:
        print('Ímpar')
        if number > 0:
            print('Positivo')
            continue
        else:
            print('Negativo')
            continue
