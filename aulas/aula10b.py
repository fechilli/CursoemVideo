n1 = float(input('digite a primeira nota: '))
n2 = float(input('sigite a segunda nota: '))
m=(n1+n2)/2
print('a sua media foi {}'.format(m))
if m>=6.0:
    print('media aprovado')
else:
    print('media baixa, reprovado')
