velo=int(input('Qual a velocidade do carro em KM? :'))
multa= (velo-80) * 7
if velo <= 80:
    print('PARABENS E BOA VIAGEM SUA VELOCIDADE É {}KM E ESTA DENTRO DO PERMITIDO'.format(velo))
else:
    print('Sua Velocidade esta acima do permitido e você pagará uma multa de R${:.2f}, mais atenção na estrada!'.format(multa))
