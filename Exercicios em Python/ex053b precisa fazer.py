nome = str(input('Digite um nome para: ')).strip().upper()
separado = nome.split()
junto = ''.join(separado)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f'É um palindromo')
else:
    print('Não é um palindromo')
