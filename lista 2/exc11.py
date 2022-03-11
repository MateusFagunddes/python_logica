""" 11.	Escreva um algoritmo para ler as notas da 1ª e 2ª avaliações de um aluno, 
calcular a média e Escreva Se este aluno foi APROVADO, REPROVADO ou Se está EM EXAME. 
Escreva também a média calculada. OBS: Para ter direito ao exame o aluno deve obter média mínima 5.5. """

avaliacao1=float(input('insira a nota primeira avaliação: '))
avaliacao2=float(input('insira a nota segunda avaliação: '))

media= (avaliacao1 + avaliacao2)/2

if media >= 8:
    print(f'parabéns você foi aprovado! Sua media foi de {media}')
elif media >= 5.5 and media < 8:
    print(f'você esta em recuperação! Sua media foi de {media}')
elif media < 5.5:
    print(f'você esta reprovado! Sua media foi de {media}')