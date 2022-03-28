""" Escrever um algoritmo que leia um número n que 
indica quantos valores devem ser lidos a seguir. 
Para cada número lido, mo=stre uma tabela contendo 
o valor lido e o fatorial deste valor.  """
fatorial = 0
n = int(input('numeros a serem lidos: '))
for i in range(1, n +1):
    num = int(input('Insira um numero a ser fatorado: '))
    contador = num
    fator = 1
    while contador > 0:
        fator *= contador
        contador -= 1
    print(f'{num}! é igual {fator}')  
