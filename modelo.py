import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Población total, N
N = float(input("Ingrese la población total: "))
# Valores iniciales de personas infectadas y recuperadas, I0 y R0
I0 = float(input("Ingrese el número inicial de personas infectadas: "))
R0 = float(input("Ingrese el número inicial de personas recuperadas: "))
# El resto de la población, suceptible a la infección
S0 = N - I0 - R0

# Tasas de transmisión y recuperación en 1/días
beta = float(input("Ingrese la tasa de transmisión (beta): "))
gamma = float(input("Ingrese la tasa de recuperación (gamma): "))

# Una cuadrícula de puntos de tiempo (en días)
dias = int(input("Ingrese el número de días a simular: "))
t = np.linspace(0, dias, dias)

# Las ecuaciones diferenciales del modelo SIR


def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt


# Vector de condiciones iniciales
y0 = S0, I0, R0

# Resolver el sistema de ecuaciones diferenciales
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T

# Graficar los datos en tres curvas separadas para S(t), I(t) y R(t)
plt.plot(t, S/N, label='Suceptibles')
plt.plot(t, I/N, label='Infectados')
plt.plot(t, R/N, label='Recuperados')
plt.xlabel('Días')
plt.ylabel('Proporción de la población')
plt.title('Modelo SIR')
plt.legend()
plt.show()

# Ahora mostremos los datos en numeros enteros para al final del tiempo de simulación
print("Suceptibles: ", int(S[dias-1]))
print("Infectados: ", int(I[dias-1]))
print("Recuperados: ", int(R[dias-1]))
