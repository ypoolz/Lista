# 23. Faça um programa que peça dois números e calcule a área correspondente à calota de duas circunferências
# concêntricas geradas pelo raio correspondentes aos dois números solicitados. Utilize a função área criada no
# exercício 22.

import math

raio1 = float(input('informe o raio do circulo1: '))
area1 = math.pi * (raio1 ** 2)
print('a area circulo1 é de: ', area1)

raio2 = float(input('informe o raio do circulo2: '))
area2 = math.pi * (raio2 ** 2)
print('a area circulo2 é de: ', area2)

calota = area1 - area2
print('a area da colota das duas curcunferencias é: ', calota)
