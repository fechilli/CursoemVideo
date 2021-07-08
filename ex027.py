nome = str (input('Digite seu nome completo: ')).strip()
print('seu nome completo é {}'.format(nome))
print('Seu primeiro nome é {}'.format(nome.split()[0]))
print('seu ultimo nome é: {}' .format(nome.split()[-1]))