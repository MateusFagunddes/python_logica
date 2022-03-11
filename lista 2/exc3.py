""" 3.	Escreva um algoritmo para ler um valor e Escreva se é POSITIVO ou NEGATIVO. 
Considere o valor zero como positivo. """

valor= float(input('insira um valor: '))

if valor > 0:
    print('o valor é '+ str(valor) + ' positivo')
elif valor < 0:
    print('o valor é '+ str(valor) + ' negativo')