""" 17.	Escreva um algoritmo para ler 3 valores e escreva a soma dos 2 maiores. 
Considere que o usuário não informará valores iguais. """

valor1= int(input('insira o valor1: '))
valor2= int(input('insira o valor2: '))
valor3= int(input('insira o valor3: '))


if valor2 > valor1 < valor3:
    print(valor2+valor3)
elif valor1 > valor2 < valor3:
    print(valor1+valor3)
else:
    print(valor1+valor2)

