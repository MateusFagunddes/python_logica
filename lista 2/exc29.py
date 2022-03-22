""" Escreva um algoritmo que leia as medidas dos lados de um triângulo e escreva 
Se ele é EQUILÁTERO, ISÓSCELES ou ESCALENO. OBS:
Equilátero: 3 lados iguais; 
Isósceles: 2 lados iguais; 
Escaleno: 3 lados diferentes.  """

lado1 = float(input("Medida do lado 1?")) 
lado2 = float(input("Medida do lado 2?")) 
lado3 = float(input("Medida do lado 3?")) 

if lado1 == lado2 == lado3: 
    print("EQUILÁTERO") 

elif (lado1 != lado2) and (lado1 != lado3) and (lado2 != lado3): 
    print("ESCALENO") 

else: 
    print("ISÓSCELES") 