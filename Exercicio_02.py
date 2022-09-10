# Criar um programa para identificar se um dia da semana (numerados de 1 a 7) é dia de semana, fim de semana
# ou um dia inválido.

dia = int(input('Digite um numero entre 1 a 7: '))

if dia == 1:
    print('Segunda')

elif dia == 2:
    print('Terça')

elif dia == 3:
    print('Quarta')

elif dia == 4:
    print('Quinta')

elif dia == 5:
    print('Sexta')

elif dia == 6:
    print('Sábado')

elif dia == 7:
    print('Domingo')

else:
    print('Número inválido')
