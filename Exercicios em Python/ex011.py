'''''''''''''''''''''
Quanto de tinta precisa para pintar a parede ?
'''''''''''''''''''''
l = float(input('Qual a largura da sua parede ? '))
a = float(input('Qual a altura da sua parede ? '))
m = float(l*a)
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.1f}m².\nVocê vai precisar de {:.1f}L de tinta para pintar a parede'.format(l, a, m, m/2))