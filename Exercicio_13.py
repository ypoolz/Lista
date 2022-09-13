# Ler um número inteiro N e calcular e imprimir todos os seus divisores. Exemplo: para o número 6, temos os seguintes divisores 1, 2, 3, 6. Utilize o laço que lhe for mais conveniente.
numero = int(input('Digite um número: '))
valor = 1

while valor < numero:
        divisao = numero % valor
        valor += 1
        if divisao == 0:
            print(valor - 1)