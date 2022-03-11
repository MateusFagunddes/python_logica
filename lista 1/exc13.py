""" A turma C é composta de 60 alunos, e a turma D de 20 alunos. 
Escreva um algoritmo que leia o percentual de alunos reprovados 
na turma C, o percentual de aprovados na turma D, calcule e escreva: 
(a) O número de alunos reprovados na turma C; 
(b) O número de alunos reprovados na turma D. 
(c) A percentagem de alunos reprovados em 
 relação ao total de alunos das duas turmas.  """

turma_c = int(60)
turma_d = int(20)

#questão a:
num_reprovados_c=int(input('insira a quantidade de alunos reprovados na turma C: '))
reprovados_turma_c= num_reprovados_c/turma_c*100
print('O percentual de reprovados na turma C é de: ' + f'{reprovados_turma_c:.2f}' + '%')

#questão b:
num_reprovados_d= int(input('insira a quantidade de alunos reprovados na turma D: '))
reprovados_turma_d= num_reprovados_d/turma_d*100
print('O percentual de reprovados na turma D é de: ' + f'{reprovados_turma_d:.2f}' + '%')

#questão c:
num_total_reprovados=(num_reprovados_c+num_reprovados_d)/(turma_c + turma_d)*100
print('O percentual de reprovação entre as duas turmas é de: '+ f'{num_total_reprovados:.2f}' + '%') 