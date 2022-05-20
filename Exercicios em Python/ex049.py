print('TABUADA!')
num = int(input('Digite um numero para vermos sua tabuada completa: '))
for c in range(1, 11):
    x = num * c
    print(f'{num} x {c} = ', end='')
    print(x)


