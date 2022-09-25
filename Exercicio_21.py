# 21. Fazer uma função que tem como parâmetros de entrada três números reais a, b, c e fornece como saída a maior
# raiz da equação do 2º grau: ax2  + bx + c = 0 Nesta questão, você deverá utilizar a fórmula de Bhaskara. Se não
# houver raízes reais, a função deve retornar o núme

def bhaskara(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    x1 = (((-1) * b) + (delta ** 0.5)) / (2 * a)
    x2 = (((-1) * b) - (delta ** 0.5)) / (2 * a)

    if delta == 0:
        print()
        print('Como delta = 0, temos um unico valor de raiz (x1 = x2): ', x1)
    elif delta > 0:
        print()
        print('Como delta > 0, temos dois valores distintos de raizes: ', x1, ' e ', x2)
    else:
        print()
        print('Como delta < 0 , não temos raizes reais!')


a = int(input('digite o valor de a: '))
b = int(input('digite o valor de b: '))
c = int(input('digite o valor de c: '))

bhaskara(a, b, c)
