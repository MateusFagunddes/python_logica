""" 10.	Coloque os elementos de um vetor dado pelo usuário 
em ordem crescente. """

lista = []
while len(lista)<=10:
    num = int(input('> '))
    if num not in lista:
        lista.append(num)
        lista.sort()
        print(lista) 
    else:
        print('numero informado já esta na lista!')