import random
a1=input("digite o nome do primeiro aluno: ")
a2=input('digite o nome do segundo aluno: ')
a3=input('digite o nome do terceiro aluno')
a4=input('digite o nome do quarto aluno: ')

lista=[a4,a3,a2,a1]
sort= random.choice(lista)
print(' oa aluno escolhido foi: {}'.format(sort))
