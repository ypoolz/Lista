#Faça um programa para ler e escrever dados de uma turma de 5 alunos. O programa deve pedir dados como
# nome, idade e sexo. O programa deve imprimir os dados do aluno mais velho. Use o laço WHILE


cont = 1 
maior_idade = 0

while cont <=5:
  print('----- ALUNO',cont,'------')
  nome = input('Nome: ')
  idade = int(input('Idade: '))
  sexo = input('Sexo [M/F]: ')

  if idade > maior_idade:
    maior_idade = idade 
    maior_nome = nome
    maior_sexo = sexo

  cont+=1

print('-- Aluno mais velho --')
print('Nome:',maior_nome, '\n' 'Idade:', maior_idade, '\n' 'Sexo:',maior_sexo)