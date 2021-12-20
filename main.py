import modulo
import numpy as np

# Comprimento lateral e vertical da placa quadrada(gera deformações caso alterado)
comprimento = 3.0

# Quantidade de nós por eixo
intervalo = 47

# Difusividade térmica
alpha = 1

# Passo de avanço no tempo
delta_t = 0.001

# Criando a matriz T para a solução numérica já com todos os valores zerados
Temp = np.zeros((intervalo+1,intervalo+1), dtype = float)

# Criando matriz T para um instante arbitrário seguinte ao da matriz Temp
Temp_new = np.copy(Temp)

# Descomentar as linhas abaixo conforme desejar usar as funções. Por padrão, a maioria está comentada para reduzir uso computacional.

# modulo.simulacao(intervalo,comprimento,alpha,Temp,Temp_new,delta_t)

# modulo.mostrar(intervalo,comprimento,Temp_new)

# modulo.analises(intervalo,comprimento,Temp_new)

modulo.simulacaoAnimada(intervalo, comprimento, alpha, Temp, Temp_new, delta_t)
