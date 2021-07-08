viagem=int(input('Qual a distância da viagem em KM: '))
dist1= viagem*0.50
dist2=viagem*0.45
if viagem > 200:
    print('o valor da passagem R${:.2f}'.format(dist2))
else:
    print('o valor da passagem R${:.2f}'.format(dist1))

