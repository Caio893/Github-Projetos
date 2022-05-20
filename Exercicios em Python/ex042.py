print('='*40)
print('Vamos Analisar Triângulos Modo Hard')
print('='*40)
r1 = float(input('Digite o primeiro valor: '))
r2 = float(input('Digite o segundo valor: '))
r3 = float(input('Digite o terceiro valor: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Podem fazer um Triangulo', end=' ')
    if r1 == r2 == r3:
        print('É um Equilátero')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES')
else:
    print('Não é um triangulo')