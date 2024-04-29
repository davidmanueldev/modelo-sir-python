import numpy as np # Importar numpy para manejo de arreglos y operaciones matemáticas en general
from scipy.integrate import odeint # Importar odeint para resolver ecuaciones diferenciales ordinarias (ODE)
import matplotlib.pyplot as plt # Importar matplotlib para graficar los resultados de la simulación de la epidemia

# Población total, N
N = float(input("Ingrese la población total: "))
# Valores iniciales de personas infectadas y recuperadas, I0 y R0
I0 = float(input("Ingrese el número inicial de personas infectadas: "))
R0 = float(input("Ingrese el número inicial de personas recuperadas: "))
# El resto de la población, suceptible a la infección
S0 = N - I0 - R0

# Tasas de transmisión y recuperación en 1/días
beta = float(input("Ingrese la tasa de transmisión (beta): ")) # La tasa de transmision es basicamente la probabilidad de que una persona infecte a otra
gamma = float(input("Ingrese la tasa de recuperación (gamma): ")) # La tasa de recuperación es la probabilidad de que una persona infectada se recupere

# Una cuadrícula de puntos de tiempo (en días)
dias = int(input("Ingrese el número de días a simular: "))
t = np.linspace(0, dias, dias) # Creamos un arreglo de 0 a dias con dias elementos ( 0, dias, dias) el primer 0 

# Las ecuaciones diferenciales del modelo SIR


def deriv(y, t, N, beta, gamma): # deriv es una función que recibe 5 argumentos, y, t, N, beta y gamma donde y es un arreglo con 3 elementos, t es el tiempo, N es la población total, beta es la tasa de transmisión y gamma es la tasa de recuperación
    S, I, R = y # y es un arreglo con 3 elementos, S, I y R
    dSdt = -beta * S * I / N # aca estamos calculando la tasa de cambio de los suceptibles con respecto al tiempo (dS/dt) y dSdt = -beta * S * I / N porque hay personas que se infectan
    dIdt = beta * S * I / N - gamma * I # aca estamos calculando la tasa de cambio de los infectados con respecto al tiempo (dI/dt) y dIdt = beta * S * I / N - gamma * I porque hay personas que se recuperan
    dRdt = gamma * I # aca estamos calculando la tasa de cambio de los recuperados con respecto al tiempo (dR/dt) y dRdt = gamma porque no hay mas personas que se recuperen
    return dSdt, dIdt, dRdt # retornamos un arreglo con las tasas de cambio de S, I y R


# Vector de condiciones iniciales
y0 = S0, I0, R0 # y0 es un arreglo con 3 elementos, S0, I0 y R0 para los suceptibles, infectados y recuperados respectivamente

# Resolver el sistema de ecuaciones diferenciales
ret = odeint(deriv, y0, t, args=(N, beta, gamma)) # ret es un arreglo con 3 columnas y dias filas, donde cada fila representa el estado de S, I y R en un tiempo t determinado, args es para pasar los argumentos adicionales a la función deriv

S, I, R = ret.T # S, I y R son arreglos con dias elementos cada uno, donde cada elemento representa el estado de S, I y R en un tiempo t determinado respectivamente, y ret.T es para transponer la matriz ret para que las filas se conviertan en columnas y viceversa
# Por si no sabian transponer es cambiar las filas por columnas y las columnas por filas

# Graficar los datos en tres curvas separadas para S(t), I(t) y R(t)
plt.plot(t, S/N, label='Suceptibles') # plt.plot es para graficar, t es el tiempo, S/N es la proporción de suceptibles con respecto a la población total
plt.plot(t, I/N, label='Infectados')
plt.plot(t, R/N, label='Recuperados')
plt.xlabel('Días') # plt.xlabel es para poner el nombre del eje x
plt.ylabel('Proporción de la población') # plt.ylabel es para poner el nombre del eje y
plt.title('Modelo SIR') # plt.title es para poner el titulo de la gráfica
plt.legend() # plt.legend es para poner la leyenda de la gráfica o sea los nombres de las curvas
plt.show() # plt.show es para mostrar la gráfica

# Ahora mostremos los datos en numeros enteros para al final del tiempo de simulación
print("Suceptibles: ", int(S[dias-1])) # el -1 es para obtener el último elemento del arreglo ya que los arreglos empiezan en 0
print("Infectados: ", int(I[dias-1])) 
print("Recuperados: ", int(R[dias-1]))
