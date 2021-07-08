from math import sqrt, ceil
cato=float(input('Digite o valor do cateto oposto: '))
cata=float(input("digite o valor do cateto adjacente: "))
hip=sqrt(cato*cato + cata*cata)
print("A hipotenusa vai medir: {:.2f}".format(hip))
