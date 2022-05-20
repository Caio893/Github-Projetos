print('='*60)
print('Vamos Calcular o preço do produto e a condição de pagamento')
print('='*60)
produto = float(input('Qual o preço do produto: '))
print('FORMA DE PAGAMENTO')
print('[ 1 ]: à vista ou cheque 10% desconto \n[ 2 ]: à vista no cartão 5% desconto', end='\n')
print('[ 3 ]: 2x no cartão sem juros \n[ 4 ]: 3x ou mais no cartão 20% de juros')
pagamento = int(input('Qual a forma de pagamento: '))
if pagamento == 1:
    print(f'Pagando á vista ou cheque você tem 10% de desconto e só paga R${produto - (produto*10/100):.2f}')
elif pagamento == 2:
    print(f'Pagando á vista no cartão você tem 5% de deconto e só paga R${produto - (produto*5/100):.2f}')
elif pagamento == 3:
    print(f'Pagando em até 2x no cartão você não paga juros ficando em 2x de R${produto / 2:.2f} por mês')
elif pagamento == 4:
    total = produto + (produto*20/100)
    totparc = int(input('Quantas parcelas: '))
    parcela = total / totparc
    print(f'Pagando em 3x ou mais no cartão você tem 20% de juros ficando em {totparc}x de R${parcela:.2f} num total de {total}')
else:
    total = 0
    print('OPÇÃO INVALIDADE DE PAGAMENTO. TENTE NOVAMENTE!')
