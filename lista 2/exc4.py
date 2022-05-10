""" 4.	Escreva um algoritmo para ler 2 valores 
(considere que não serão informados valores iguais) 
e escreva o maior deles. """

valor1= float(input('insira o valor1: '))
valor2= float(input('insira o valor2: '))
if valor1!= valor2:
    if valor1 > valor2:
        print('valor1 é maior que o valor2')
    else:
        print('valor2 é maior que o valor1')
else:
    print('valores iguais!')