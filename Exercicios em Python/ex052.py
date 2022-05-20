print('Numeros Primos')
num1 = int(input('Digite um número: '))
tot = 0
for c in range(1, num1 + 1):
    if num1 % c ==0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end=' ')
print(f'O numero {num1} foi divisivel por {tot} vezes')
if tot ==2:
    print(f'E por isso ele É  PRIMO!')
else:
    print(f'E por isso ele NÃO É PRIMO!')