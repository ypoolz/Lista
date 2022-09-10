# Crietrue=Noneama que verifica se um número inteiro informado pelo usuário é divisível por 3.


def check(number):
    return number / 3


n = int(input('Type a number: '))
if check(n):
    print("Yes")
else:
    print("No")
