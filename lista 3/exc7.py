""" Escreva um algoritmo que calcule a média aritmética das 3 
notas dos alunos de uma classe. O algoritmo deverá ler, 
além das notas, o código do aluno e deverá ser encerrado 
quando o código for igual a zero.  """

cod_aluno = -1
while cod_aluno != 0 :
    cod_aluno = int(input('Insira o codigo do aluno: '))
    if cod_aluno != 0:
        nota1 = float(input('Insira a nota 1a: '))
        nota2 = float(input('Insira a nota 2a: '))
        nota3 = float(input('Insira a nota 3a: '))
        media = (nota1 + nota2 + nota3)/3
        print(f'A média de entres as três notas do aluno {cod_aluno} é {media:.2f}')
    else:
        break