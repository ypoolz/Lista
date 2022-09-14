x = int(input('Digite um número inteiro: '))
maior = x

for i in range(9):
    x = int(input('Digite um número inteiro: '))

    if x > maior:
        maior = x
print('O maior valor digitado foi', maior)