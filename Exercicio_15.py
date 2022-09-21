# Escreva um programa capaz de ler o saldo inicial de uma conta bancária e um número indeterminado de
# operações de depósito e saque. O usuário deve digitar “1” para realizar um depósito, “2” para realizar um saque e
# “0” para encerrar o programa apresentando o saldo final e uma mensagem “Programa encerrado”.

salario = int(input('Digite seu saldo inicial: '))

deposito = 0
saque = 0

while salario:
    print('====== Operação ======')
    print('Digite 0 para encerrar o programa''\n''Digite 1 para depósito''\n''Digite 2 para saque')

    op = int(input('Digite qual opção deseja realizar: '))

    if op == 1:
        deposito = int(input('Quanto deseja depositar: '))
        salario += deposito
        print('-----DEPÓSITO REALIZADO COM SUCESSO----')
        print('Seu saldo é de:', 'R$', salario)
        continue

    elif op == 2:
        saque = int(input('Quanto deseja sacar: '))
        salario -= saque
        print('-----SAQUE REALIZADO COM SUCESSO----')
        print('Seu saldo é de:', 'R$', salario)
        continue

    else:
        print('----PROGRAMA ENCERRADO----')
        print('Saldo final','R$', salario)
        break
