nome = str(input('Digite seu nome completo: ')).strip()
primeiro = nome.split()
print('Seu primeiro nome é {}'.format(primeiro[0]))
print('Seu ultimo nome é {}'.format(primeiro[len(primeiro)-1]))