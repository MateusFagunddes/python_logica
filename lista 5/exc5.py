""" 13. Função para retornar o perímetro e a área (com parâmetro). """

def cAreaPerimetro(lados_poligonos,medida_do_lado):
    perimetro_triangulo= medida_do_lado*lados_poligonos
    area_quadrado= medida_do_lado**2

    if lados_poligonos == 3 or lados_poligonos == 4 or lados_poligonos == 5:
        if lados_poligonos == 3:
            print(f'O triângulo em um perimetro de {perimetro_triangulo}')
        elif lados_poligonos == 4:
            print(f'O quadrado tem uma area de {area_quadrado}')
        elif lados_poligonos == 5:
            print('É um pentágono') 
    else:
        print('Insira um valor de lados entre 3, 4 ou 5!')
        
cAreaPerimetro(3,5)