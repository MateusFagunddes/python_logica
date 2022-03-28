""" Escrever um algoritmo que leia 20 valores para uma variável n e, 
para cada um deles, calcule a tabuada de 1 até n. Mostre a tabuada na forma: 
1 x n = n 
2 x n = 2n 
3 x n = 3n  
... 
n x n = n2  """

num = int(input('digite uma tabuada: '))
for i in range(1,11):
    resultado =  num*i 
    print(f'{num} x {i} = {resultado}')
