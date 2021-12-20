import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.animation as animation
import math
import time

def simulacao(intervalo, comprimento, alpha, Temp, Temp_new, delta_t):
	delta_x = (comprimento) / intervalo
	fourier = alpha*(delta_t) / ((delta_x)**2)
	print(fourier)
	if(fourier > 0.25):
		print("Simulação abortada.\nNúmero de fourier acima ou igual a 0.25.\n Simulação instável.\n")
		return 0
	
#	Condição inicial da placa de temperatura
	Temp[math.floor(2/delta_x), math.floor(1/delta_x) -1 : math.floor(2/delta_x) +1] = 10
	Temp[math.floor(1/delta_x), math.floor(1/delta_x) -1 : math.floor(2/delta_x) +1] = 100
	Temp[math.floor(1/delta_x) : math.floor(2/delta_x),math.floor(1/delta_x)] = 10
	Temp[math.floor(1/delta_x) : math.floor(2/delta_x) ,math.floor(2/delta_x)] = 10
	Temp[:,math.floor(0/delta_x)] = 100
	Temp[math.floor(0/delta_x),:] = 100
	Temp[:,math.floor(3/delta_x)] = 100
	Temp[math.floor(3/delta_x),:] = 100
	
#	Criação da pasta para armazenamento de frames individuais()
	try:
		os.mkdir('./imagens')
	except:
		print()

#	Solução transiente
	for k in range(99000):#Loop para o tempo
		for i in range(intervalo +1): #Loop na direção x
			for j in range(intervalo +1): #Loop na direção y
				Temp_new[j, i] = Temp[j, i]*(1-(4*fourier))
				if(Temp_new[j, i]<0):
					Temp_new[j, i] = 0
				if(i<intervalo):
					Temp_new[j, i] += (fourier*Temp[j, i+1])
				if(i!=0):
					Temp_new[j, i] += (fourier*Temp[j, i-1])
				if(j<intervalo):
					Temp_new[j, i] += (fourier*Temp[j+1, i])
				if(j!=0):
					Temp_new[j, i] += (fourier*Temp[j-1, i])

#	Seção de condicionais para garantir condições de contorno
				if( math.floor(1/delta_x) -1 < i and i < math.floor(2/delta_x) +1 and j == math.floor(2/delta_x)):
					Temp_new[j, i] = 10
				if( math.floor(1/delta_x) -1 < i and i < math.floor(2/delta_x) +1 and j == math.floor(1/delta_x)):
					Temp_new[j, i] = 100
				if( math.floor(1/delta_x) < j and j < math.floor(2/delta_x) and i == math.floor(1/delta_x)):
					Temp_new[j, i] = 10
				if( math.floor(1/delta_x) < j and j < math.floor(2/delta_x) and i == math.floor(2/delta_x)):
					Temp_new[j, i] = 10
				if( math.floor(0/delta_x) == i ):
					Temp_new[j, i] = 100
				if( math.floor(0/delta_x) == j ):
					Temp_new[j, i] = 100
				if( math.floor(3/delta_x) == i ):
					Temp_new[j, i] = 100
				if( math.floor(3/delta_x) == j ):
					Temp_new[j, i] = 100
				if( math.floor(1/delta_x) < i and i < math.floor(2/delta_x) and math.floor(1/delta_x) < j and j < math.floor(2/delta_x)):
					Temp_new[j, i] = 0

		Temp = np.copy(Temp_new)

#   Utilizar a linha comentada abaixo para gerar imagens para cada seção do tempo
#	em uma pasta chamada 'imagens' em mesmo local de arquivo de execução
#		plt.imsave('./imagens/' + str(k) + '.png', np.flipud(Temp_new), cmap='hot')
#	Condição de parada
		if(abs(Temp_new[math.floor(0.5/delta_x),math.floor(1.5/delta_x)] - Temp[math.floor(0.5/delta_x),math.floor(1.5/delta_x)]) < 0.01/(intervalo**2)
		and Temp_new[math.floor(0.5/delta_x),math.floor(1.5/delta_x)] > 96):
			break
	return 1

def mostrar(intervalo, comprimento, Temp_new):
#	Plotar gráfico
	plt.figure()
	plt.title('Malha de '+ str(intervalo) + 'x' + str(intervalo))
	plt.xlabel('Comprimento(m)')
	plt.ylabel('Comprimento(m)')
	plt.imshow(np.flipud(Temp_new), cmap='hot', interpolation='none', extent=[0, comprimento, 0, comprimento])
	clp = plt.colorbar()
	clp.set_label('Temperatura(K)', color = 'firebrick')
	plt.show()

def analises(intervalo, comprimento, Temp_new):
#	Região de código utilizado para análises de domínios de cálculo
	delta_x = comprimento / intervalo
	domCalcx = np.zeros(intervalo +1, dtype = float)
	domCalcy = np.zeros(intervalo +1, dtype = float)
	
	fig, imgs = plt.subplots(2, 2)

	for x in range(intervalo +1):
		domCalcx[math.floor(x)] = x*delta_x
		domCalcy[math.floor(x)] = Temp_new[x, math.floor(0.5/delta_x)]
	imgs[0,0].plot(domCalcx, domCalcy)
	imgs[0,0].set_title('Análise em eixo y=0.5 fixado')

	for x in range(intervalo +1):
		domCalcx[math.floor(x)] = x*delta_x
		domCalcy[math.floor(x)] = Temp_new[x, math.floor(1.5/delta_x)]
	imgs[0,1].plot(domCalcx, domCalcy)
	imgs[0,1].set_title('Análise em eixo y=1.5 fixado')

	for x in range(intervalo +1):
		domCalcx[math.floor(x)] = x*delta_x
		domCalcy[math.floor(x)] = Temp_new[x, math.floor(2/delta_x)]
	imgs[1,0].plot(domCalcx, domCalcy)
	imgs[1,0].set_title('Análise em eixo y=2 fixado')

	for x in range(intervalo +1):
		domCalcx[math.floor(x)] = x*delta_x
		domCalcy[math.floor(x)] = Temp_new[x, math.floor(2.5/delta_x)]
	imgs[1,1].plot(domCalcx, domCalcy)
	imgs[1,1].set_title('Análise em eixo y=2.5 fixado')

	plt.show()

def simulacaoAnimada(intervalo, comprimento, alpha, Temp, Temp_new, delta_t):
	delta_x = (comprimento) / intervalo
	fourier = alpha*(delta_t) / ((delta_x)**2)
	print(fourier)

#	Propriedades para a animação
	fig = plt.figure()
	ims = []

	if(fourier > 0.25):
		print("Simulação abortada.\nNúmero de fourier acima ou igual a 0.25.\n Simulação instável.\n")
		return 0
#	Condição inicial da placa de temperatura
	Temp[math.floor(2/delta_x), math.floor(1/delta_x) -1 : math.floor(2/delta_x) +1] = 10
	Temp[math.floor(1/delta_x), math.floor(1/delta_x) -1 : math.floor(2/delta_x) +1] = 100
	Temp[math.floor(1/delta_x) : math.floor(2/delta_x),math.floor(1/delta_x)] = 10
	Temp[math.floor(1/delta_x) : math.floor(2/delta_x) ,math.floor(2/delta_x)] = 10
	Temp[:,math.floor(0/delta_x)] = 100
	Temp[math.floor(0/delta_x),:] = 100
	Temp[:,math.floor(3/delta_x)] = 100
	Temp[math.floor(3/delta_x),:] = 100

#	Solução transiente
	for k in range(99000):#Loop para o tempo
		for i in range(intervalo +1): #Loop na direção x
			for j in range(intervalo +1): #Loop na direção y
				Temp_new[j, i] = Temp[j, i]*(1-(4*fourier))
				if(Temp_new[j, i]<0):
					Temp_new[j, i] = 0
				if(i<intervalo):
					Temp_new[j, i] += (fourier*Temp[j, i+1])
				if(i!=0):
					Temp_new[j, i] += (fourier*Temp[j, i-1])
				if(j<intervalo):
					Temp_new[j, i] += (fourier*Temp[j+1, i])
				if(j!=0):
					Temp_new[j, i] += (fourier*Temp[j-1, i])

#	Seção de condicionais para garantir condições de contorno
				if( math.floor(1/delta_x) -1 < i and i < math.floor(2/delta_x) +1 and j == math.floor(2/delta_x)):
					Temp_new[j, i] = 10
				if( math.floor(1/delta_x) -1 < i and i < math.floor(2/delta_x) +1 and j == math.floor(1/delta_x)):
					Temp_new[j, i] = 100
				if( math.floor(1/delta_x) < j and j < math.floor(2/delta_x) and i == math.floor(1/delta_x)):
					Temp_new[j, i] = 10
				if( math.floor(1/delta_x) < j and j < math.floor(2/delta_x) and i == math.floor(2/delta_x)):
					Temp_new[j, i] = 10
				if( math.floor(0/delta_x) == i ):
					Temp_new[j, i] = 100
				if( math.floor(0/delta_x) == j ):
					Temp_new[j, i] = 100
				if( math.floor(3/delta_x) == i ):
					Temp_new[j, i] = 100
				if( math.floor(3/delta_x) == j ):
					Temp_new[j, i] = 100
				if( math.floor(1/delta_x) < i and i < math.floor(2/delta_x) and math.floor(1/delta_x) < j and j < math.floor(2/delta_x)):
					Temp_new[j, i] = 0
		Temp = np.copy(Temp_new)
		im = plt.imshow(np.flip(Temp_new), animated=True, cmap='hot', interpolation='none', extent=[0, comprimento, 0, comprimento])
		ims.append([im])

#	Condição de parada
		if(abs(Temp_new[math.floor(0.5/delta_x), math.floor(1.5/delta_x)] - Temp[math.floor(0.5/delta_x), math.floor(1.5/delta_x)]) < 0.01/(intervalo**2)
		and Temp_new[math.floor(0.5/delta_x), math.floor(1.5/delta_x)] > 96):
			break

#	Montagem da animação com todas as imagens 'im' salvadas em 'ims[]'
	ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True, repeat_delay=1000)
	plt.title('Malha de '+ str(intervalo) + 'x' + str(intervalo))
	plt.xlabel('Comprimento(m)')
	plt.ylabel('Comprimento(m)')
	clp = plt.colorbar()
	clp.set_label('Temperatura(K)', color = 'firebrick')
	ani.save('animacaoteste.mp4')
	plt.show()
	return 1
