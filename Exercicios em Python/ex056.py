velho = 0
nomevelho = 0
novo = 0
media = 0
mulher_nova = 0

for c in range(1, 5):
    print(f'-----{c}ª PESSOA -----')
    nome = str(input('Qual é o seu nome: ')).strip().upper()
    idade = int(input('Qual a sua idade: '))
    sexo = str(input('SEXO [M/F]: ')).strip().upper()
    media += idade

    if c == 1 and sexo in 'Mm':
        velho = idade
        nomevelho = nome
        novo = idade
    if sexo in 'Mm' and idade > velho:
        velho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher_nova =+ 1

print(f'A média de idade do grupo é de {media/c:.0f} anos')
print(f'O mais velho do grupo tem {velho} anos de idade e se chama {nomevelho}')
print(f'Ao todo são {mulher_nova} mulheres com menos de 20 anos.')