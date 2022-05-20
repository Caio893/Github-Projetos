produto = float(input('Qual o preço do produto ? R$'))
print('O produto que custava R${0} na promoção de 5% de desconta fica em R${1:.2f}'.format(produto,produto - (produto*5/100)))
