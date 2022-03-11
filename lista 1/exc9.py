""" Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, 
calcular e escrever o valor correspondente em graus Celsius: C = ((F – 32)*5)/9 """

graus_Fahrenheit= int(input('insira a temperatura em graus Fahrenheit: '))

temperatura_celsius= ((graus_Fahrenheit - 32)*5)/9

print('a conversão de graus Fahrenheit em Celsius é: ' + str(temperatura_celsius)+ 'C')