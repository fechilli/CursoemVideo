from time import sleep
ano=int(input('Digite um ano: '))
print('vamos advinhar se ele é bi sexto...')
sleep(2)
if (ano%4 == 0 and ano % 100!=0 or ano % 400 == 0 ):
    print('o ano de {} é bissexto'.format(ano))

else:
    print('O ano {} nao é bissexto'.format(ano))

