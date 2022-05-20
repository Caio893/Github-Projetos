num = float(input('Digite a distancia da sua viajem: '))
if num > 200:
    print(f'Sua viagem vai custar R${num * 0.45:.2f}')
else:
    print(f'Sua viagem vai custar R${num * 0.50:.2f}')