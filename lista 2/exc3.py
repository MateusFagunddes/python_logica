""" 3.	Escreva um algoritmo para ler um valor e Escreva se é POSITIVO ou NEGATIVO. 
Considere o valor zero como positivo. """

valor= int(input('insira um valor: '))

if valor >= 0:
    print('o valor é positivo')
elif valor < 0:
    print('o valor é negativo')