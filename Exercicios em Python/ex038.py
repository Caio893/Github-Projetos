num = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
if num > num2:
    print(f'O {num} é maior que o {num2}')
elif num2 > num:
    print(f'{num2} é maior que o {num}')
elif num == num2:
    print('Eles tem o mesmo valor.')