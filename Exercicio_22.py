# Faça uma função chamada area que calcula de uma circunferência. Utilize o valor de π fornecido pelo módulo math.

import math


def area(raio):
    circunferencia = 2 * math.pi * raio
    return circunferencia


r = float(input('informe o raio do circulo: '))
print('a circunferencia circulo é de: ', (area(r)))
