""" 6.	As maçãs custam R$ 0,30 ser forem compradas menos do que uma dúzia, 
e R$ 0,25 ser forem compradas pelo menos doze.  Escreva um algoritmo que 
leia o número de maçãs compradas, calcule e escreva o valor total da compra. """

preco_maca_menos12= float(0.30)
preco_maca_mais12= float(0.25)

macas_compradas= int(input('insira a quantidade de maças compradas: '))
valor_a_pagar=float()

if macas_compradas >= 12:
    valor_a_pagar= preco_maca_mais12 * macas_compradas
    print('o valor da compra de maças é de: ' + str(valor_a_pagar))
else:
    valor_a_pagar= preco_maca_menos12 * macas_compradas
    print('o valor da compra de maças é de: ' + str(valor_a_pagar))

