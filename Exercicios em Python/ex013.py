salario = float(input('Qual é o salário do funcionário ? R$'))
aumento = (salario * 15/100)
print('O salario do funcionário de R${} teve um aumento de R${:.2f} por causa do aumento de 15%. '.format(salario, aumento), end='')
print('Ficando no total de {:.2f}'.format(aumento + salario))