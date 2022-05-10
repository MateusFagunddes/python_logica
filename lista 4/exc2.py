""" 2.	Solicite ao usuário 10 números inteiros, guarde-os 
em um vetor e em seguida imprima-os na tela. Em seguida 
conte quantos elementos são negativos e informe ao usuário. """

lista = list(range(10))
contador = 0
for i in lista:
    n = int(input(f'{i +1}ᵒn: '))
    lista[i] = n

print(lista)

for i in lista:
    if i < 0:
        contador += 1
print(f'a quantidade de numeros negativos na lista é de : {contador}')
             