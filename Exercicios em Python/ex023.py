num = int(input('Digite um valor: '))
n = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
x = num // 1000 % 10
print('Analisando o numero tal {}'.format(num))
print('Unidade: {}'.format(n))
print('Dezenas: {}'.format(d))
print('Centena {}'.format(c))
print('Milhar: {}'.format(x))