num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão: ')
print('[ 1 ] Converter para BINÁRIO \n[ 2 ] Converter para OCTAL \n[ 3 ] Converter para HEXADECIMAL')
con = int(input('Sua Opção: '))
if con == 1:
    print(f'{num} convertido para BINÁRIO é igual a {num :b}')
elif con == 2:
    print(f'{num} convertido para OCTAL é igual a {num :o}')
elif con == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {num :x}')
else:
    print('Alguma coisa deu errado porvarfor tente novamente.')