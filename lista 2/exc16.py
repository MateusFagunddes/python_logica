""" 16.	Escreva um algoritmo para ler 3 valores e escreva o maior deles. 
Considere que o usuário não informará valores iguais. """

valor1= float(input('insira o valor1: '))
valor2= float(input('insira o valor2: '))
valor3= float(input('insira o valor3: '))

if valor1> valor2 and valor1 >valor3:
    print(f'o valor mais alto é o  valor1 e ele vale {valor1}')

if valor2> valor1 and valor2 >valor3:
    print(f'o valor mais alto é o valor2 e ele vale{valor2}')

if valor3> valor2 and valor3 >valor1:
    print(f'o valor mais alto é o valor3 e ele vale{valor3}')