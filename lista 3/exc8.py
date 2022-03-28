""" Escreva um algoritmo que calcule a média dos números 
digitados pelo usuário, se eles forem pares. 
Termine a leitura se o usuário digitar zero (0).  """
num = 0
soma = 0
contador = 1
while True:
    num = int(input('numero:  '))
    if num != 0:
        if num % 2 == 0:
            soma += num
            media = soma / contador
            print(f'A média de entres os numeros digitados é {media}')
            contador += 1
    else:
        break
