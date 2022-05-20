nota1 = float(input('Qual foi sua primeira nota: '))
nota2 = float(input('Qual foi a sua segunda nota: '))
media = (nota1 + nota2) / 2
if media <= 5.0:
    print(f'Você foi REPROVADO sua média foi {media} boa sorte na próxima vez! ')
elif 7 > media >=5:
    print(f'Sua Média foi {media} e ficou de RECUPERAÇÃO estude mais !')
elif media >= 7.0:
    print(f'Sua média foi {media} você foi APROVADO !')
