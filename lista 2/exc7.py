""" 7.	Escreva um algoritmo para ler 2 valores 
(considere que não serão lidos valores iguais) 
e escrevê-los em ordem crescente. """

valor1=int(input('insira o valor1: '))
valor2=int(input('insira o valor2: '))
if valor1 != valor2:
    if valor1 < valor2:
        print(f'{valor1} ,{valor2}')
    else:
        print(f'{valor2} ,{valor1}')
else:
    print('os numeros não pode ser igual!')




