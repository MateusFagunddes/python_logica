""" Escreva um algoritmo para ler as 4 notas obtidas 
por um aluno em 4 avaliações. Calcular a média usando 
a seguinte fórmula:  
#Média = (N1 + (N2 * 2) + (N3 * 3) + N4) / 7 

A seguir imprima o conceito do aluno baseado na seguinte tabela: 

A = 9,0 ou acima de 9,0 
B = entre 7,5 (inclusive) e 9,0 
C = entre 6,0 (inclusive) e 7,5  
D = abaixo de 6,0  """

n1 = float(input('Insira a nota n1: '))
n2 = float(input('Insira a nota n2: '))
n3 = float(input('Insira a nota n3: '))
n4 = float(input('Insira a nota n4: '))
media = (n1 + (n2 * 2) + (n3 * 3) + n4) / 7 

if media >= 9.0:
    print(f'Parabéns você tirou nota {media:.2f}, conceito A!')

if media >= 7.5 and media < 9:
    print(f'Parabéns você tirou nota {media:.2f}, conceito B!')

if media >= 6 and media < 7.5:
    print(f'Você tirou nota {media:.2f}, conceito C!')

if media < 6:
    print(f'Você tirou nota {media:.2f}, conceito D! Estude mais!')
