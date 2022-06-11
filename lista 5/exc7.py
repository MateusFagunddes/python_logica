""" 20. Procedimento para determinar o quadrante do ponto x e y (com parâmetro). """

def planoCartesiano(x,y):
    if x != 0 and y != 0:
        if (x > 0) and (y > 0):
            return 'você esta no primeiro quadrante'

        elif (x < 0) and (y > 0):
            return 'você esta no segundo quadrante'

        elif (x < 0) and (y < 0):
            return 'você esta no terceiro quadrante'

        elif (x > 0) and (y < 0):
            return 'você esta no quarto quadrante'
    else:
        return 'não esta em nenhum quadrante!'


print(planoCartesiano(5,1))#primeiro quadrante
print(planoCartesiano(-5,1))#segundo quadrante
print(planoCartesiano(-5,-1))#terceiro quadrante
print(planoCartesiano(5,-1))#quarto quadrante