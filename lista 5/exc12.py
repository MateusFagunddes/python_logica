""" 15. Função para determinar o intervalo do número lido (com parâmetro) 
e Procedimento que mostrará a quantidade de números em cada intervalo. """

def intervalo(num):
    if num >=0:
        if num >=0 and num <=25:
            print(f'o valor {num} esta entre 0 e 25')
        if num >=26 and num <=50:
            print(f'o valor {num} esta entre 26 e 50')
        if num >=51 and num <=75:
            print(f'o valor {num} esta entre 51 e 75')
        if num >=76 and num <=100:
            print(f'o valor {num} esta entre 76 e 100')
 

intervalo(15)