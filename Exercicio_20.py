# 20 Fazer uma função chamada somatória que tem como parâmetro de entrada um número inteiro positivo N e
# fornece como saída a soma de todos os números inteiros positivos menores ou iguais a N.
# Exemplo: se N for 3, a função deve retornar 6, que é a soma de 1 + 2 + 3

numero = int(input('informe um numero: '))
somatoria = 0
while (numero > 0):
    somatoria = somatoria + numero
    numero = numero - 1
print('o resultado da somatoria é: ', somatoria)
