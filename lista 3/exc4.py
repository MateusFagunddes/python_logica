""" Chico tem 1,50 metro e cresce 4 centímetros por ano, 
enquanto Zé tem 1,30 metro e cresce 6 centímetros por ano. 
Construa um algoritmo que calcule e imprima quantos anos serão 
necessários para que Zé seja maior que Chico.  """

chico = float(1.50)
Zé = float(1.30)
contador = 0

while Zé < chico:
    chico += 0.04
    Zé += 0.06
    contador +=1
contador +=1
print(contador)
