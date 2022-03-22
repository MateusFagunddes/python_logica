""" Escreva um algoritmo para ler as coordenadas (X,Y) de um ponto no 
sistema cartesiano e Escreva o quadrante ao qual o ponto pertence. 
Se o ponto estiver sobre os eixos, ou na origem, Escreva NÃO ESTÁ EM 
NENHUM QUADRANTE. Considere que o usuário poderá informar qualquer 
valor para as coordenadas.  """

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
    print('não esta em nehum quadrante!')


