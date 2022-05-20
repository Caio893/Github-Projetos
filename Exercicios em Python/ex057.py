n = 'S'
while n != 'M' or 'F':
    n = str(input('Qual é o seu sexo M de Masculino ou F de Feminino: ')).upper()[0] #[0] Só pega a primeira letra;
    if n == 'M':
        print('Seu sexo é Masculino')
        break
    if n == 'F':
        print('Seu sexo é Feminino')
        break
    print('Dados invalidos. Por favor, informe seu sexo: ')
print('Fim')
