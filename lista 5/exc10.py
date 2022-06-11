""" 11. Função que retorno o resultado da equação através de parâmetros. """

def pa(a1,n,r):
    soma = 0
    for i in range(a1, n *r, r):
        soma += i
    return f'primeiro termo: {a1}\nquantidade de termos: {n}\nrazão: {r}\nA soma dos termos da progressão é de {soma}'

print(pa(0,10,5))