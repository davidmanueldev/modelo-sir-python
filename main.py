import numpy as np
from scipy.integrate import odeint
import plotly.graph_objects as go

# Solicitar datos al usuario
N = float(input("Ingrese la población total, N: "))
I0 = float(input("Ingrese el número inicial de infectados, I0: "))
R0 = float(input("Ingrese el número inicial de recuperados, R0: "))
beta = float(input("Ingrese la tasa de transmisión, alfa: "))
gamma = float(input("Ingrese la tasa de recuperación, beta: "))
dias = int(input("Ingrese la cantidad de días para la simulación: "))

# El resto de la población, S0, es susceptible a la infección inicialmente.
S0 = N - I0 - R0

# Puntos en la gráfica (en días)
t = np.linspace(0, dias, dias)

# Las ecuaciones diferenciales del modelo SIR.
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# Vector de condiciones iniciales
y0 = S0, I0, R0
# Resolver el sistema de ecuaciones diferenciales, en la secuencia de días que ya definimos
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T

# Redondear los valores
S = np.round(S)
I = np.round(I)
R = np.round(R)

# Crear figura para visualización
fig = go.Figure()

# Agregar trazas para susceptibles, infectados y recuperados
fig.add_trace(go.Scatter(x=t, y=S, mode='lines', name='Susceptibles',
                         hovertemplate='Día: %{x}<br>Susceptibles: %{y:.0f}<extra></extra>'))
fig.add_trace(go.Scatter(x=t, y=I, mode='lines', name='Infectados',
                         hovertemplate='Día: %{x}<br>Infectados: %{y:.0f}<extra></extra>'))
fig.add_trace(go.Scatter(x=t, y=R, mode='lines', name='Recuperados',
                         hovertemplate='Día: %{x}<br>Recuperados: %{y:.0f}<extra></extra>'))

# Mejorar la presentación
fig.update_layout(title='Evolución de la pandemia: Modelo SIR',
                  xaxis_title='Días',
                  yaxis_title='Número de personas',
                  legend_title='Grupos')

# Mostrar el gráfico
fig.show()

# 1000, 1,0, 0.3313, 0.0833, 120
