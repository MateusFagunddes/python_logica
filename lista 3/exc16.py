""" Escrever um algoritmo que lê um conjunto não 
determinado de valores, um de cada vez, 
e escreve uma tabela com cabeçalho, que deve ser 
repetido a cada 20 linhas. A tabela conterá o valor 
lido, seu quadrado, seu cubo e sua raiz quadrada.  """

from math import sqrt
while True:
    print('____'*20)
    print(' A tabela com o valor lido, seu quadrado, seu cubo e sua raiz quadrada.')
    print('____'*20)
    for i in range(1,5):
        num = int(input('valor: '))
        quadrado_num = num **2
        cubo_num = num **3
        raiz_num= sqrt(num)
        print(f'o valor informado foi: {num}')
        print(f'seu quadrado é: {quadrado_num}')
        print(f'seu cubo é: {cubo_num}')
        print(f'sua raiz quadrada é: {raiz_num}')
