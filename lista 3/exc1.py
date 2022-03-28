""" Escrever um algoritmo que lê 5 valores para a, um de cada vez, 
e conta quantos destes valores são negativos, escrevendo esta 
informação.   """

for i in range(1,6):
    num = int(input('insira um valor: '))
    if num < 0:
        print(f'{num} é negativo')