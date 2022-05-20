soma = 0
cout = 0
for c in range(1, 501, 2):
    if c % 3 ==0:
        cout = cout + 1
        soma = soma + c
print(f'A soma de todos os valores solicitados é a {soma} e a conta de todos os valores é {cout}')
