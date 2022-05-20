print('='*40)
print('Vamos Calcular seu IMC!!!')
print('='*40)
altura = float(input('Qual a sua altura: '))
peso = float(input('Qual o seu peso: '))
IMC = peso / (altura**2)
print(f'O IMC dessa pessoa é de {IMC:.2f}')
if IMC < 18.5:
    print('Você esta abaixo do Peso!')
elif 18.5 <= IMC <= 24.9:
    print('Você esta no peso NORMAL!')
elif 25.0 <= IMC <= 29.9:
    print('Você esta com SOBREPESO!')
elif 30.0 <= IMC <= 39.9:
    print('Você esta com OBESIDADE')
elif IMC >= 40.0:
    print('Você esta OBESIDADE GRAVE!!')
