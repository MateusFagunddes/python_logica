""" Escreva um algoritmo para ler uma temperatura em graus Celsius, calcular e escrever
 o valor correspondente em graus Fahrenheit: F = C * 9 / 5 + 32 """

temperatura_celsius= int(input('insira a temperatura em graus Celsius: '))
temperatura_Fahrenheit= ((temperatura_celsius * 9) / 5) + 32


print('a conversão de graus Fahrenheit em Celsius é: ' + str(temperatura_Fahrenheit)+ 'F')