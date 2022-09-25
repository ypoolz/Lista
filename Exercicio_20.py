# 20 Fazer uma função chamada somatória que tem como parâmetro de entrada um número inteiro positivo N e
# fornece como saída a soma de todos os números inteiros positivos menores ou iguais a N.
# Exemplo: se N for 3, a função deve retornar 6, que é a soma de 1 + 2 + 3

def somatoria(n):
    soma = 0
    for i in range (n,0,-1):
        soma += i
    return soma

num = int(input('Digite um numero: '))

print(somatoria(num))