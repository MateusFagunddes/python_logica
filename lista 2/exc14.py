""" 14.	Acrescente as seguintes mensagens à solução do exercício anterior conforme o caso.
(a)	Caso o número de lados seja inferior a 3 Escreva: NÃO E UM POLÍGONO. 
(b)	Caso o número de lados seja superior a 5 Escreva: POLÍGONO NÃO IDENTIFICADO.
OBS: Considere que o usuário poderá informar qualquer valor para o número de lados.
 """

lados_poligonos=int(input('quantos lados tem este poligono: '))
medida_do_lado = float(input('quanto medirá o seu poligono? '))

if lados_poligonos == 3:
    perimetro_triangulo= medida_do_lado*lados_poligonos
    print(f'O triângulo tem um perimetro de {perimetro_triangulo}')

elif lados_poligonos == 4:
    area_quadrado= medida_do_lado**2
    print(f'O quadrado tem uma area de {area_quadrado}')

elif lados_poligonos == 5:
    print('é um pentágono!')

elif lados_poligonos < 3:
    print('não é um poligono!')
elif lados_poligonos > 5:
    print('poligono nao identificado!')
