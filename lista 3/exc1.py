""" Escrever um algoritmo que lê 5 valores para a, um de cada vez, 
e conta quantos destes valores são negativos, escrevendo esta 
informação.   """
contador = 0
for i in range(5):
    num = int(input('insira um valor: '))
    if num < 0:
        contador+=1
print(f'{contador} numeros informados são negativos')