import random
from time import sleep
print('<>' * 30)
print('Vamos jogar irei pensar em um número entre 0 e 5. tente adivinhar')
print('<>' * 30)
chute = int(input('Digite o núemro que eu pensei? '))
print('processando...')
sleep(2)
num= random.randint(0,5)
if chute == num:
    print('PARABENS, VOCE ACERTOU, o numero escolhido era {}'.format(num))
else:
    print('GANHEI, eu pensei no número {} e você digitou {}' .format(num,chute))
