""" 26.	Escreva um algoritmo que leia 500 valores inteiros e positivos e:  
      a) encontre o maior valor;
      b) encontre o menor valor;
      c) calcule a média dos números lidos.
 """
menor_numero = 99**99
maior_numero = 0
soma = 0

for i in range(1,501):
    numero = int(input(f'{i}ᵒ numero:'))
    soma += numero

    if numero > maior_numero:
        maior_numero = numero
    if numero < menor_numero:
        menor_numero = numero

media = soma /500

print(f'a media dos 500 valores lidos é {media}')
print(f'menor valor lido: {menor_numero}')
print(f'maior valor lido: {maior_numero}')

