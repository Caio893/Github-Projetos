from datetime import date
ano = int(input('Digite um ano para saber se ele é BISSEXTO ou tecle 0 para saber o ano atual da sua máquina: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 == 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} NÃO é BISSEXTO')