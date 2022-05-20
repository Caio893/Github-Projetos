from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensa num numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
pc = randint(0, 5)
print('PROCESSANDO....')
sleep(5)
print('O numero em que eu pensei é {}'.format(pc))
if jogador == pc:
    print('NOSSA COMO VOCÊ SABIA QUE EU ESTAVA PENSANDO ISSO ?!')
else:
    print('Boa Sorte na próxima vez.')
