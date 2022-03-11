""" 7.	Escreva um algoritmo para ler 2 valores 
(considere que não serão lidos valores iguais) 
e escrevê-los em ordem crescente. """

valor=[int(input('insira o valor1: ')), int(input('insira o valor2: '))]
if valor[0] != valor[1]:
    valor.sort()
    print(valor)
else:
    print('os valores não podem ser iguai!')







