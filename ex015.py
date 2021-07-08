km=float(input('Qantos km foram percorridos?'))
dias=int(input('quantos dias de locação?'))
total=(dias*60)+(km*0.15)
print('Ovalor a pagar será de R${:.2f}'.format(total))
