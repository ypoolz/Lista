# 21. Fazer uma função que tem como parâmetros de entrada três números reais a, b, c e fornece como saída a maior
# raiz da equação do 2º grau: ax2  + bx + c = 0 Nesta questão, você deverá utilizar a fórmula de Bhaskara. Se não
# houver raízes reais, a função deve retornar o número −1.

a = float(input('Entre com o valor de a: '))
b = float(input('Entre com o valor de b: '))
c = float(input('Entre com o valor de c: '))

delta = (b ** 2) - 4 * a * c

if a == 0:
    print("O valor de a, deve ser diferente de 0")
elif delta < 0:
    print("Sem raízes reais", -1)
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    print("x1: {}, x2: {}".format(x1, x2))
