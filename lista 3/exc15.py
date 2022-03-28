""" Escrever um algoritmo que leia uma quantidade desconhecida 
de números e conte quantos deles estão nos seguintes 
intervalos: [0.25], [26,50], [51,75] e [76,100]. 
A entrada de dados deve terminar quando for lido um número negativo.  """

while True:
    num = float(input('Valor: '))
    if num >=0:
        if num >=0 and num <=25:
            print(f'o valor {num} esta entre 0 e 25')
        if num >=26 and num <=50:
            print(f'o valor {num} esta entre 26 e 50')
        if num >=51 and num <=75:
            print(f'o valor {num} esta entre 51 e 75')
        if num >=76 and num <=100:
            print(f'o valor {num} esta entre 76 e 100')
    else:
        break    