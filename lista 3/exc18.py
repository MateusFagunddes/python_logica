""" Escrever um algoritmo que lê um número não determinado de valores 
para m, todos inteiros e positivos, um de cada vez. 
Se m for par, verificar quantos divisores possui e escrever esta informação. 
Se m for ímpar e menor do que 10 calcular e escrever o fatorial de m. 
Se m for ímpar e maior ou igual a 10 calcular e escrever a soma dos inteiros de 1 até m.  """
contador =0 
while True:
    m = int(input('valor: '))
    if m % 2 == 0:
        for i in range(m , 0, -1):
            p = m / i   
            if p % 2 ==0:
                contador +=1
        print(contador) 



