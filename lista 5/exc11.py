""" 12. Função que retorna a multiplicação de cada número da tabuada (com parâmetros). """

def tabuada(num):
    for i in range(1,11):
        resultado =  num*i 
        print(f'{num} x {i} = {resultado}')

tabuada(5)