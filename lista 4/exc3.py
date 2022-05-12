""" 3.	Leia um vetor de 10 elementos e em seguida ache a 
posição do elemento com o valor dado pelo usuário dentro do vetor. 
Caso o elemento não exista no vetor informe ao usuário. """

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:
    num_informado = int(input('> '))
    if num_informado in lista:
        print(f'o índice do valor informado é: {lista.index(num_informado)}')
    else:
        print('valor não encontrado!')

