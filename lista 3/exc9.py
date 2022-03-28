""" Escreva um algoritmo que leia 50 valores 
e encontre o maior e o menor deles. Mostre o resultado.  """

maior = 0
menor = 10**100
for i in range(0,50):
    num = int(input('valor: '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f'maior: {maior} e menor: {menor}')