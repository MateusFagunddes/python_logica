""" 10. Função para retornar se o número é par 
ou ímpar (com parâmetro). """

def nPar(num):
    if num%2 ==0:
        return f'{num} é par'
    else:
        return f'{num} é impar'

print(nPar(4))
print(nPar(3))
