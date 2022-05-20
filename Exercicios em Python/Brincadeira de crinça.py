frase = str(input('Digite um texto ou frase para ser analisada da forma que o programador definir. ')).strip().upper()
x = str(input('Digite oque você quer procurar nesse texto ou frase. '))
y = frase.count(x.upper().strip())
print('Oque você procurou aparece {} vezes no texto. '.format(y))