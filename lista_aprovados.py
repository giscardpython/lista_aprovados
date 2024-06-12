#Crie um programa que cadastre o nome de 30 alunos em uma lista, e receba de cada aluno 5 notas de 0 a 10. 
# O programa deverá retornar a média do aluno e indicar se o aluno está aprovado ou reprovado (média para aprovação = 7). Ao final, o programa deverá mostrar uma lista com o nome dos aprovados. Crie um repositório, suba no GitHub e poste o link.

import os

# a lista de alunos
alunos = []
nota1 = []
nota2 = []
nota3 = []
nota4 = []
nota5 = []
media = []
i = 0

while i < 2:
    # informa o nome da nova fruta 
    novo_aluno = str(input('\nInsira o nome do Aluno: ').upper())
    nota1_aluno = float(input('\nInsira a nota 1 do Aluno: '))
    nota2_aluno = float(input('\nInsira a nota 2 do Aluno: '))
    nota3_aluno = float(input('\nInsira a nota 3 do Aluno: '))
    nota4_aluno = float(input('\nInsira a nota 4 do Aluno: '))
    nota5_aluno = float(input('\nInsira a nota 5 do Aluno: '))
    alunos.append(novo_aluno)
    nota1.append(nota1_aluno)
    nota2.append(nota2_aluno)
    nota3.append(nota3_aluno)
    nota4.append(nota4_aluno)
    nota5.append(nota5_aluno)
     
    print(f'\nNome do Aluno: ', alunos[i])

    print(f'Nota 1 do Aluno: ', nota1[i])
    print(f'Nota 2 do Aluno: ', nota2[i])
    print(f'Nota 3 do Aluno: ', nota3[i])
    print(f'Nota 4 do Aluno: ', nota4[i])
    print(f'Nota 5 do Aluno: ', nota5[i])
    media_aluno = (nota1[i] + nota2[i] + nota3[i] + nota4[i] + nota5[i]) / 5
    #media_aluno = 8
    media_aluno = float(media_aluno)

    print(f'Média do Aluno: ', media_aluno)
    media.append(media_aluno)
    num = i + 1
    if media_aluno >= 7:
        print(f'{num}o nome da lista: {alunos[i]} está aprovado')
    else:
        print(f'{num}o nome da lista: {alunos[i]} está reprovado')


    i +=1
    continue

i = 0
print('\nLista de Aprovados: ')
for aluno in alunos:
    if media[i] >= 7:
        print(f'{alunos[i]}')
    i +=1

 


