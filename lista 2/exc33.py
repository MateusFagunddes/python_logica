""" Para participar da categoria OURO do 1º Campeonato Mundial de 
Bolinha de Gude o jogador deve pesar entre 70 Kg (inclusive) 
e 80 Kg (inclusive) e medir de 1,75 m (inclusive) a 1,90 m 
(inclusive). Escreva um algoritmo para ler a altura e o peso 
de um jogador e determine Se o jogador está apto a participar do 
campeonato escrevendo uma das seguintes mensagens conforme cada 
situação.  
a. ‘RECUSADO POR ALTURA’: Se somente a altura do jogador for inválida 
b. ‘RECUSADO POR PESO’: Se somente o peso do jogador for inválido 
c. ‘TOTALMENTE RECUSADO’: Se a altura e o peso do jogador forem inválidos 
d. ‘ACEITO': Se a altura e o peso do jogador estiverem dentro da faixa especificada  """

peso = float(input('Insira uma valor para o peso: '))
altura =float(input('Insira uma valor para a altura: '))
pesoideal = 0
alturaideal = 0

if peso >= 70 and peso <= 80:
    pesoideal = peso
else:
   print('RECUSADO POR PESO') 

if altura >= 1.75 and altura <= 1.90:
    alturaideal = altura
else:
    print('RECUSADO POR ALTURA')

if peso == pesoideal and altura == alturaideal:
    print('ACEITO')

    



