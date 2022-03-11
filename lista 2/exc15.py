""" 15.	Escreva um algoritmo para ler 2 valores e uma das seguintes operações a serem executadas 
(codificada da seguinte forma: 1.Adição, 2.Subtração, 3.Divisão, 4.Multiplicação). 
Calcular e Escreva o resultado dessa operação sobre os dois valores lidos. """
valor1= float(input('insira o valor1: '))
valor2= float(input('insira o valor2: '))

operacoes= int(input('insira qual a operação deseja realizar 1.Adição, 2.Subtração, 3.Divisão, 4.Multiplicação: '))
if operacoes < 1 or operacoes >4:
    print('operação não cadastrada!')

if operacoes== 1:
    adicao= valor1 + valor2
    print(f'o resultado da adição é {adicao}')

if operacoes== 2:
    subtracao= valor1 - valor2
    print(f'o resultado da subtracao é {subtracao}')

if operacoes== 3:
    divisao= valor1 / valor2
    print(f'o resultado da divisao é {divisao}')

if operacoes== 4:
    multiplicacao= valor1 * valor2
    print(f'o resultado da multiplicacao é {multiplicacao}')