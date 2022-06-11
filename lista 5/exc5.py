""" 13. Função para retornar o perímetro e a área (com parâmetro). """

def cAreaPerimetro(lados_poligonos,medida_do_lado):
    perimetro_triangulo= medida_do_lado*lados_poligonos
    area_quadrado= medida_do_lado**2

    if lados_poligonos == 3 or lados_poligonos == 4 or lados_poligonos == 5:
        if lados_poligonos == 3:
            return f'O triângulo em um perimetro de {perimetro_triangulo}'
        elif lados_poligonos == 4:
            return f'O quadrado tem uma area de {area_quadrado}'
        elif lados_poligonos == 5:
            return 'É um pentágono' 
    else:
        return 'Insira um valor de lados entre 3, 4 ou 5!'.upper()
        
print(cAreaPerimetro(3,6))#triangulo
print(cAreaPerimetro(4,6))#quadrado
print(cAreaPerimetro(5,6))#pentágono

print(cAreaPerimetro(6,6))#valor de lados invalido