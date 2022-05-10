""" 28.	Escrever um algoritmo que calcule e mostre 
a média aritmética dos números lidos entre 13 e 73. """
armazena_soma = 0
termo1 = 0
for i in range(13,74):
    armazena_soma += i
media = armazena_soma / 60
print(f'media aritmética dos numeros entre 13 e 73 é {media}') 