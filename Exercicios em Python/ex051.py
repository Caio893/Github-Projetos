print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
num = int(input('Digite o termo: '))
num2 = int(input('Digite uma razão: '))
dec = num + (10 - 1) * num2
for c in range(num, dec + num2, num2):
    print(c, end='-> ')
    print('ACABOU!')