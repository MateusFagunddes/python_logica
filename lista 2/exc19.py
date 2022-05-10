""" 19.	Escreva um algoritmo para ler as coordenadas (X,Y) de um 
ponto no sistema cartesiano e  Escreva o quadrante ao qual o 
ponto pertence.  Considere que o usuário não informará nenhuma 
coordenada  igual a zero. """

x= int(input('insira a coordenada x: '))
y= int(input('insira a coordenada y: '))

if x == 0 or y==0:
    print('as coordenadas não podem conter um valor ZERO!')

if (x > 0) and (y > 0):
    print('você esta no primeiro quadrante')

elif (x < 0) and (y > 0):
   print('você esta no segundo quadrante')

elif (x < 0) and (y < 0):
    print('você esta no terceiro quadrante')

elif (x > 0) and (y < 0):
    print('você esta no quarto quadrante')
    
