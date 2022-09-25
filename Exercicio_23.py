# 23. Faça um programa que peça dois números e calcule a área correspondente à calota de duas circunferências
# concêntricas geradas pelo raio correspondentes aos dois números solicitados. Utilize a função área criada no
# exercício 22.

import math

def area (raio):
  area = math.pi * raio**2
  return area


r1 = float(input('informe o raio do 1º circulo: '))
print ('a circunferencia circulo é de: ', int(area(r1)))

r2 = float(input('informe o raio do 2º circulo: '))
print ('a circunferencia circulo é de: ', int(area(r2)))

z = area(r1)-area(r2)

print('a area correspondente a colota das duas curcunferencias concentricas é: ', z)