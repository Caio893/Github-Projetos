from datetime import date
atleta_ano = int(input('Qual o ano de nascimento do atleta: '))
ano_atual = date.today().year
idade = ano_atual - atleta_ano
if idade <= 9:
    print(f'O Atleta tem {idade} Anos Classificação: MIRIM')
elif 14 >= idade >= 10:
    print(f'O Atleta tem {idade} Anos Classificação: INFANTIL')
elif 19 >= idade >= 15:
    print(f'O Atleta tem {idade} Anos Classificação: JÚNIOR')
elif 25 >= idade >=20:
    print(f'O Atleta tem {idade} Anos Classificação: SÊNIOR')
else:
    print(f'O Atleta tem {idade} Anos Classificação: MASTER')
