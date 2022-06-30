import modulo
import numpy as np
import sys

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return True

# Comprimento lateral e vertical da placa quadrada (gera deformações caso alterado)
comprimento = 3.0

# Quantidade de nós por eixo (-n seguido do valor de nos para mudar)
intervalo = 47

# Difusividade térmica
alpha = 1

# Passo de avanço no tempo (-t seguido do valor de passo para mudar)
delta_t = 0.001

# Criando a matriz T para a solução numérica já com todos os valores zerados
Temp = np.zeros((intervalo+1,intervalo+1), dtype = float)

# Criando matriz T para um instante arbitrário seguinte ao da matriz Temp
Temp_new = np.copy(Temp)

# Coletando argumentos na chamada do codigo
arg = sys.argv[1:]

try:
    index_node = arg.index("-n")
except ValueError:
    index_node = -1
if(index_node != -1 and is_integer(arg[index_node + 1])):
    intervalo = int(arg[index_node + 1])
    
try:
    index_time = arg.index("-t")
except ValueError:
    index_time = -1   
if(index_time != -1 and is_number(arg[index_time + 1])):
    delta_t = float(arg[index_time + 1])

# Descomentar as linhas abaixo conforme desejar usar as funções. Por padrão, a maioria está comentada para reduzir uso computacional.

# modulo.simulacao(intervalo,comprimento,alpha,Temp,Temp_new,delta_t)

# modulo.mostrar(intervalo,comprimento,Temp_new)

# modulo.analises(intervalo,comprimento,Temp_new)

modulo.simulacaoAnimada(intervalo, comprimento, alpha, Temp, Temp_new, delta_t)
