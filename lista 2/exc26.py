""" Escreva um algoritmo para ler as coordenadas (X,Y) de um 
ponto no sistema cartesiano e Escreva o quadrante ao qual o 
ponto pertence. Caso o ponto não pertença a nenhum quadrante, 
escreva se ele está sobre o eixo X, eixo Y ou na origem. Considere 
que o usuário poderá informar qualquer valor para as coordenadas.  """

x= int(input('insira a coordenada x: '))
y= int(input('insira a coordenada y: '))

if x != 0 and y != 0:
    if (x > 0) and (y > 0):
        print('você esta no primeiro quadrante')

    elif (x < 0) and (y > 0):
        print('você esta no segundo quadrante')

    elif (x < 0) and (y < 0):
        print('você esta no terceiro quadrante')

    elif (x > 0) and (y < 0):
        print('você esta no quarto quadrante')
else:
    if x ==0:
        if y > 0 or y < 0:
            print('você esta sobre o eixo y porem não pertence a nenhum quadrante!')
    if y ==0:
        if x > 0 or x < 0:
            print('você esta sobre o eixo x porem não pertence a nenhum quadrante!')	

if x == 0 and y ==0:
    print('você esta na origem!') 
