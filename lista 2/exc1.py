""" 1.	Escreva um algoritmo para ler as notas das duas avaliações de um aluno no semestre, 
calcular e Escreva a média semestral e a seguinte mensagem: ‘PARABÉNS! Você foi aprovado’ 
somente Se o aluno foi aprovado (considere 8.0 a nota mínima para aprovação). """

avaliacao1= float(input('informe a nota da avaliação1: '))
avaliacao2= float(input('informe a nota da avaliação2: '))

media_Nota= (avaliacao1 + avaliacao2)/2

if media_Nota >= 8.0:
    print('PARABÉNS! Você foi aprovado')
