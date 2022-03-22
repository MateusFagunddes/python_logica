""" Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Alcool 
    até 20 litros 3%
    mais de 20 5%

Gasolina
    Até 15 litros 3,5% 
    mais de 15 litros 6%

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível 
(codificado da seguinte forma: 1-álcool 2-Gasolina), calcule e imprima o valor a 
ser pago pelo cliente, sabendo-se que o preço da gasolina é de R$ 1,90 o litro e 
o álcool R$ 1,28. """

alcool= 1.28
gasolina= 1.90

tipoCombustivel= int(input('Insira o combustivel: [1-álcool 2-Gasolina] '))
litrosVendidos= int(input('Insira a quantidade de litros vendida: '))

if tipoCombustivel == 1 :
    if litrosVendidos <= 20:
        pagar= ((alcool * 0.03) + alcool) * litrosVendidos
        print(f'o valor total a pagar é de R${pagar:.2f}. Foram consumidos {litrosVendidos}')
    else:
        pagar= ((alcool * 0.05) + alcool) * litrosVendidos
        print(f'o valor total a pagar é de R${pagar:.2f}. Foram consumidos {litrosVendidos}')

if tipoCombustivel == 2:
    if litrosVendidos <= 15:
        pagar= ((gasolina * 0.035) + gasolina) * litrosVendidos
        print(f'o valor total a pagar é de R${pagar:.2f}. Foram consumidos {litrosVendidos}')
    else:
        pagar= ((gasolina * 0.06) + gasolina) * litrosVendidos
        print(f'o valor total a pagar é de R${pagar:.2f}. Foram consumidos {litrosVendidos}')
