a = int(input('Primeir Valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Terceiro Valor: '))
#Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor valor digitado foi o {menor} ')
print(f'O maior valor digitado foi o {maior}')
