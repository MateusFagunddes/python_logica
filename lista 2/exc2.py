""" 2.	Acrescente ao exercício acima a mensagem ‘Você foi REPROVADO! Estude mais.’ 
caso a média calculada seja menor que 8,0. """

avaliacao1= float(input('informe a nota da avaliação1: '))
avaliacao2= float(input('informe a nota da avaliação2: '))

media_Nota= (avaliacao1 + avaliacao2)/2

if media_Nota >= 8.0:
    print('PARABÉNS! Você foi aprovado')
else:
    print('Você foi REPROVADO! Estude mais.')