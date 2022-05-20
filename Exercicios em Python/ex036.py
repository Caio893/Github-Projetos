casa = float(input('Qual o valor da Casa: '))
salario = float(input('Qual o salário da pessoa que vai fincananciar: '))
tempo = float(input('E em quanto anos ele vai pagar a casa: '))
if casa/(tempo*12) > (salario*30/100):
    print(f'Para pagar uma casa de R${casa:.0f} em {tempo:.0f} anos a prestação será de {casa/(tempo*12):.0f} por mês superando 30% do seu salário que é R${salario*30/100:.2f}.')
else:
    print(f'Parabéns ! Você conseguiu seu empréstimo ! Agora você pode comprar a sua casa pagando R${casa/tempo*12:.2f} por mês durante {tempo:.0f} anos!')
