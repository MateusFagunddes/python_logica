""" Função para retornar o preço das maças (com parâmetro). """

def cMaca(macas_compradas):
    preco_maca_menos12= float(0.30)
    preco_maca_mais12= float(0.25)

    if macas_compradas >= 12:
        valor_a_pagar= preco_maca_mais12 * macas_compradas
        return f'o valor da compra de maças é de: R$ {valor_a_pagar:.2f}'
    else:
        valor_a_pagar= preco_maca_menos12 * macas_compradas
        return f'o valor da compra de maças é de: R$ {valor_a_pagar:.2f}'

print(cMaca(12))
print(cMaca(9))