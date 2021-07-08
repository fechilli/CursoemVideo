import math
ang=float(input('Digite o ângulo que voce deseja: '))
ang=math.radians(ang)
seno= math.sin(ang)
cos= math.cos(ang)
tang= math.tan(ang)
print('o ângulo de {} tem o SENO: {:.2f}'.format(ang, seno))
print('o ângulo de {} tem o COSSENO {:.2f}'.format(ang, cos))
print('o ângulo de {} tem a TANGENTE {:.2f}' . format(ang, tang))
