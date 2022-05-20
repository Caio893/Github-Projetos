from random import randint
erro = 0
print('Jogo da adivinhação\nTente adivinhar qual numero o computador estapensando')
pc = randint(0, 10)
jogador = int(input('Digite um numero: '))
while jogador != pc:
    if jogador > pc:
        print('Menos... Tente mais uma vez.')
    if jogador < pc:
        print('Mais... Tente mais uma vez.')
    jogador = int(input('Tente outros numeros até acertar !: '))
    erro +=1
print(f'Parabéns o {pc} foi oque o computador estava pensando. E você tentou {erro}x vezes')
#ultima aula de Python no Curso em Video