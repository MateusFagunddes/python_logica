""" Escreva um algoritmo que leia o código de um aluno e suas três notas.
 Calcule a média ponderada do aluno, considerando que o peso para a 
 maior nota seja 4 e para as duas restantes, 3. Mostre o código do 
 aluno, suas três notas, a média calculada e uma mensagem "APROVADO"
 se a média for maior ou igual a 5 e "REPROVADO" se a média for menor
  que 5. Repita a operação até que o código lido seja negativo.  """

cod_aluno = 0
peso1 = 4
peso2 = peso3 = 3

while True :
    cod_aluno = int(input('Insira o codigo do aluno: '))
    if cod_aluno > 0:
        nota1 = float(input('Insira a nota 1a: '))
        nota2 = float(input('Insira a nota 2a: '))
        nota3 = float(input('Insira a nota 3a: '))
        soma_media  = (nota1 * peso1) +(nota2 * peso2) + (nota3 * peso3)
        divisao_media = soma_media / (peso1 + peso2 + peso3) 
        media_ponderada = divisao_media
        print(f'A média de entre as três notas do aluno {cod_aluno} é {media_ponderada:.2f}')
        if media_ponderada >= 5:
            print(f'Aluno {cod_aluno} APROVADO!')
        else:
            print(f'Aluno {cod_aluno} REPROVADO!')
    else:
        break