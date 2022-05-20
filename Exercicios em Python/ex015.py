dia = int(input('Por quantos dias o carro foi alugado ? '))
km = float(input('Quatos kilometros o carro percorreu ? '))
valor = (dia * 60) + (km * 0.15)
print('O custo total foi de R${:.2f}'.format(valor))