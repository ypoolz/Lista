# Escreva um programa que leia um conjunto de 10 números inteiros positivos. Seu programa deve determinar e imprimir
# o maior deles. Use o laço FOR.

x = int(input('Digite um número inteiro: '))
maior = x

for i in range(9):
    x = int(input('Digite um número inteiro: '))

    if x > maior:
        maior = x
print('O maior valor digitado foi', maior)
