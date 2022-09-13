# A seguinte sequência de números 0, 1, 1, 2, 3, 5, 8, 13, 21... é conhecida como série de Fibonacci. Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores. Escreva um algoritmo que leia um inteiro N (onde N < 46) e mostre os N primeiros números dessa série. Utilize o laço que lhe for mais conveniente. 
x = 0
n = 0
print ('Sequência de fibonacci')
while(n < 46):
    print(n)
    n = n + x
    x = n - x
    if(n == 0):
        n = n + 1