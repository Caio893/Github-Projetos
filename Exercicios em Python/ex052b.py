num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        tot = tot + 1
        print(c)
print(f'O numero foi divido {tot}x')
if tot==2:
    print('É PRIMO!')
else:
    print('Não é primo')