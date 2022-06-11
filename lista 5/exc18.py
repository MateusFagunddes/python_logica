""" 10. Procedimento que troca os valores com as 
posições indicadas por parâmetro. """

def listaCrescente():
    lista = []
    while len(lista)<=9:
        num = int(input('> '))
        if num not in lista:
            lista.append(num)
            lista.sort()
            return lista 
        else:
            return 'numero informado já esta na lista!'


listaCrescente()