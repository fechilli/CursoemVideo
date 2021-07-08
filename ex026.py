frase = str (input('digite uma frase: ')).strip().upper()

print('a letra a aparece {} vezes'.format(frase.count("A")))
print('Ela aparece na posição {} pela primeira vez' .format(frase.find('A')+1))
print( 'Ela aparece na posição {} pela ultima vez'.format(frase.rfind('A')+1))

'estive cara à cara'
