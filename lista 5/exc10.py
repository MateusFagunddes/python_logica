""" 11. Função que retorno o resultado da equação através de parâmetros. """

def pa(a1,n,r):
    soma = 0
    for i in range(a1, n *r+1, r):
        print(i, end = ', ')
        soma += i
    print(f'a soma dos termos da progressào é de {soma}')

pa(0,10,5)