print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Digite um valor: '))
r2 = float(input('Digite um valor: '))
r3 = float(input('Digite um valor: '))
if r3 - r2 < r1 < r3 + r2 and r1 - r2 < r3 < r2 + r1 and r1 - r3 < r2 < r1 + r3:
    print('É possivel fazer um triangulo')
else:
    print('Não é prossivel fazer um triangulo')