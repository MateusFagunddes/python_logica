""" Escrever um algoritmo que leia um número não determinado 
de valores e calcule a média aritmética dos valores lidos, 
a quantidade de valores positivos, a quantidade de valores 
negativos e o percentual de valores negativos e positivos. 
Mostre os resultados.  """
valor_positivo = valor_negativo = contador = soma = 0

while True:
    num = int(input('valor: '))

    if num >=0:
        valor_positivo +=1
    if num <0:
        valor_negativo +=1

    contador += 1  
    soma = soma + num
    media = soma / contador
    perc_valor_negativo = (valor_negativo * 100)/ contador
    perc_valor_positivo = (valor_positivo * 100)/ contador
    print(f'a media dos valores informados é {media:.2f}')
    print(f'a quantidade de valores positivos informados foi de {valor_positivo} isso representa {perc_valor_positivo:.2f}% do todal informado({contador})')
    print(f'a quantidade de valores negativo informados foi de {valor_negativo} isso representa {perc_valor_negativo:.2f}% do todal informado({contador})')
