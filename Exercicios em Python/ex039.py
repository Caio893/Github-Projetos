from datetime import date
nascimento = int(input('Em que ano o candidato nasceu: '))
ano = date.today().year
idade = ano - nascimento
feminino = str(input('Você é do sexo feminno SIM ou NÃO ')).strip().upper()
if idade == 18 and feminino == 'NÃO, NAO':
    print(f'Você está com {idade} anos idade procure uma junta Militar para seu alistamento.')
    print(f'Você nasceu em {nascimento} \nSeu alistamento é em {ano}')
elif idade > 18 and feminino == 'NÃO, NAO':
    print(f'Você tem {idade} anos, passou a idade para o alistamento o ano para seu alistamento foi em {(18 - idade) + ano}.')
    print(f'Você nasceu em {nascimento}')
elif idade < 18 and feminino == 'NÃO, NAO':
    print(f'Você ainda não idade para o alistamento Militar você tem {idade} anos de idade, ainda faltam {18 - idade} anos para seu alistamento.')
    print(f'O ano para seu alistamento vai ser em {18 - idade + ano}')
else:
    print('Você não precisa fazer alistamento Militar Obrigatório')