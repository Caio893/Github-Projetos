'''frase = str(input('Digite sua frase para podermos analisá-la: ')).strip().upper()
num = frase.count('A')
num2 = frase.find('A')+1
num3 = frase.rfind('A')+1
print('A letra A aparece {} vezes na frase'.format(num))
print('A primeira letra A apareceu na posição {}'.format(num2))
print('A última letra A apareceu na posição {}'.format(num3))'''
frase = str(input('Digite uma frase para se analisada: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A letra A aparece pela primeira vez na posição {}.'.format(frase.find('A')+1))
print('A letra A aparece pela ultima vez na posição {}.'.format(frase.rfind('A')+1))