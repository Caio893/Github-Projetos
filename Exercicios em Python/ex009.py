medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
dm = medida * 10
km = medida / 1000
hm = medida / 100
dam = medida / 10
print('A Transfomação de Unidade de {} metros \n{:.0f} cm \n{:.0f} mm \n{:.0f} dm'.format(medida, cm, mm, dm), end='')
print('\n{}km \n{} hm \n{} dam'.format(medida, km, hm, dam))
