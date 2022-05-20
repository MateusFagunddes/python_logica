""" 20. Procedimento para determinar o quadrante do ponto x e y (com parâmetro). """

def planoCartesiano(x,y):
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


planoCartesiano(5,1)
planoCartesiano(-5,1)
planoCartesiano(-5,-1)
planoCartesiano(5,-1)