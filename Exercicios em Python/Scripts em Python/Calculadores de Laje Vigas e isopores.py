totmetro = 0
totisopor = 0
totvigas = 0
totvalor = 0
valorlaje = float(input('Preço do Metro²: '))
comodos = int(input('Quantidade de Comodos: '))
for c in range(1, comodos+1):
    print(f'------------{c}º Comodo------------')
    viga = float(input('Informe o Viga: '))
    vao = float(input('Informe a Vão: '))

    metro = viga * vao
    totmetro += metro

    valor = metro * valorlaje
    totvalor += valor
    if vao % 0.43 == 4 or 5 or 6 or 7 or 8 or 9:
        vigas = 1 + (vao / 0.43)
        totvigas += vigas

    isopor = vigas * viga
    totisopor += isopor


    print(f'O Metro Quadrado é {metro:.1f}')
    print(f'Preço da Laje fica em {valor:.1f}')
    print(f'Vigas são {vigas:.0f} de {viga:.1f} Metros')
    print(f'Isopores {isopor:.1f}')
print('='*40)
print(f'O metro quadrado total fica em {totmetro:.2f}M²\nO preço total fica em R${totvalor:.2f}', end='')
print(f'\nCom um total de {totvigas:.0f} Vigas \nE {totisopor:.1f} Isopores. ')
