''' 4.	Solicite ao usuário dois vetores de 5 números 
e em seguida calcule a soma dos vetores, elemento
 a elemento, em um terceiro vetor. '''

lista1 = list(range(5))
lista2 = list(range(5))
lista_soma = list(range(5))

for i  in lista1:
    n = int(input(f'lista1, valor{i+1}: '))
    lista1[i] = n

print(f'lista 1: {lista1}')

for i  in lista2:
    n = int(input(f'lista2, valor{i+1}: '))
    lista2[i] = n
print(f'lista 2: {lista2}')

for i in lista_soma:
    lista_soma[i] = lista1[i] + lista2[i]

print(f'a lista contendo a soma entre lista1 e lista2 vale: {lista_soma}')