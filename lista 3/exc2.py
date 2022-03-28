""" Escrever um algoritmo que lê um valor N 
inteiro e positivo e que calcula e escreve o valor de SOMA.
SOMA = 1 + 1 / 1 + 1 / 2 + 1 / 3 + 1 / N 
"""
while True:
    N = int(input('insira um valor positivo: '))
    if N >= 0:
        soma =  (1+1) / (1+1)/ (2+1)/ (3+1)/N
        print(soma) 
    else:
        print('o valor informado é negativo!') 
