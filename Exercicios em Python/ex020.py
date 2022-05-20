from random import shuffle
n1 = str(input('Qual o nome da primeira pessoa: '))
n2 = str(input('Qual o nome da segunda pessoa: '))
n3 = str(input('Qual o nome da terceira pessoa: '))
n4 = str(input('Qual o nome da quarta pessoa: '))
resultado = [n1, n2, n3, n4]
shuffle(resultado)
print('A ordem de quem vai ser morto sera')
print(resultado)

