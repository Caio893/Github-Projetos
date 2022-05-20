salario = float(input('Digite o valor do seu salário: '))
if salario >= 1250.00:
    print(f'O seu aumento de salário foi de {salario + (salario*10/100):.2f}')
else:
    print(f'O seu aumento de salário foi de {salario + (salario*15/100):.2f}')