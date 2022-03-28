""" Construir um algoritmo que calcule a média aritmética de 
vários valores inteiros positivos, lidos externamente. 
O final da leitura acontecerá quando for lido um valor negativo."""
resultado = 0
soma = 0
contador = 1
num = 1
while num > 0:
    print('-_=_'*20)
    num = int(input('insira um valor: '))
    soma = soma + num
    resultado = soma / contador
    contador += 1
    print(f'a media dos numeros fornecidos é de {resultado}')
    print(f'some mais uma valor a {num} ou informe um valor negativo para encerrar a aplicação!')
