""" 10.	Escreva um algoritmo para ler um número inteiro 
(considere que serão lidos apenas valores positivos e inteiros) 
e Escreva se é PAR ou ÍMPAR.  """

num=int(input('insira um numero: '))

if num>=0:
    if num % 2 == 0:
        print(str(num) + ' é par')
    else:
        print(str(num) + ' é impar')
else:
    print('informe um valor positivo!')        