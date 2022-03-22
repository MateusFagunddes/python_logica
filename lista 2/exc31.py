""" Escreva um algoritmo que leia o valor de 3 ângulos de um triângulo e escreva 
Se o triângulo é ACUTÂNGULO, RETÂNGULO ou OBTUSÂNGULO. OBS: 
Retângulo: um ângulo reto. 
Obtusângulo: um ângulo obtuso; 
Acutângulo: 3 ângulos agudos.  """

angulo1= int(input('insira o angulo 1: '))
angulo2= int(input('insira o angulo 2: '))
angulo3= int(input('insira o angulo 3: '))

#angulo reto 90 graus
#angulo obtuso > 90 graus
#angulo agudo < 90 graus

#ACUTÂNGULO  todos os agulos menos que 90 graus
#RETÂNGULO   um algulo reto 
#OBTUSÂNGULO possui um dos seus ângulos internos com medida maior que 90° e menor que 180°

if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
    print('é um triangulo acutangulo')

if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
    print('é um triangulo retangulo')

if angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
    print('é um triangulo abtusangulo')

