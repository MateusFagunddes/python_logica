""" Escreva um algoritmo que leia um número n 
(número de termos de uma progressão aritmética), 
a1 (o primeiro termo da progressão) e r (a razão da progressão) 
e escreva os n termos desta progressão, bem como a soma dos elementos.   

An = a1 + (n-1).r """

n = int(input('número de termos de uma progressão aritmética: '))
a1 = int(input('o primeiro termo da progressão: '))
r = int(input("a razão da progressão: "))
soma = 0
for i in range(a1, n *r+1, r):
    print(i, end = ', ')
    soma += i
print(f'a soma dos termos da progressào é de {soma}')
