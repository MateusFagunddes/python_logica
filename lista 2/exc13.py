""" 13.	Escreva um algoritmo para ler o número de lados de um polígono regular, e a medida do lado. Calcular e imprimir o seguinte: 
(a)	Se o número de lados for igual a 3, Escreva: TRIÂNGULO e o valor do seu perímetro; 
(b)	Se o número de lados for igual a 4 Escreva: QUADRADO e o valor da sua área;
(c)	Se o número de lados for igual a 5 Escreva: PENTÁGONO.
OBS: Considere que o usuário só informará os valores 3,4 ou 5.
 """


lados_poligonos= int(input('quantos lados tem este poligono: '))
medida_do_lado= float(input('qual a medida dos lados do poligono: '))

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