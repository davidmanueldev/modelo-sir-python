# import matplotlib.pyplot as plt
# import numpy as np
# import matplotlib.animation as animation
# from IPython.display import HTML

# N = 10**3

# h = 25/(N-1)

# t = [0]
# S = [995]
# I = [5]
# R = [0]

# α = 0.0014
# β = 0.6

# for n in range(N):
#   t.append(t[n]+h)
#   S.append(S[n] - h*α*I[n]*S[n] )
#   I.append(I[n] + h*( α*I[n]*S[n] - β*I[n] ))
#   R.append(R[n]+ h*β*I[n])

# plt.plot(t,S, label = "S(t)")
# plt.plot(t,I, label = "I(t)")
# plt.plot(t,R, label = "R(t)")
# plt.legend()
# plt.title("Propagación de una infección", fontweight="bold", size = 20)
# plt.grid()
# plt.show()

# fig=plt.figure()
# ax=fig.gca()

# def actualizar(i):
#   ax.clear()

#   ax.plot(t[:i], S[:i],'-', label= "Suceptible")
#   ax.plot(t[:i], I[:i],'-', label= "Infectado")
#   ax.plot(t[:i], R[:i],'-', label= "Recuperado")
#   ax.set_title("Propagación de una infección", fontweight="bold", size = 20)
#   ax.set_xlabel("Tiempo", fontweight="bold", size = 15)
#   ax.grid(True)
#   ax.plot(t[i],  S[i],'o',markersize=10,color='r')
#   ax.plot(t[i],  I[i],'o',markersize=10,color='r')
#   ax.plot(t[i],  R[i],'o',markersize=10,color='r')
#   ax.legend()

# ani=animation.FuncAnimation(fig, actualizar, range(0,N), interval=50)
# HTML(ani.to_html5_video())

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from IPython.display import HTML

# Solicitar al usuario que ingrese los parámetros y valores iniciales
N = int(input("Ingrese el tamaño de la población (N): "))
S0 = float(input("Ingrese el número inicial de susceptibles (S0): "))
I0 = float(input("Ingrese el número inicial de infectados (I0): "))
R0 = float(input("Ingrese el número inicial de recuperados (R0): "))

# Tiempo de simulación
t_max = int(input("Ingrese el tiempo máximo de simulación: "))
h = 25 / (N - 1)

# Parámetros de la ecuación diferencial
α = float(input("Ingrese el valor de α: "))
β = float(input("Ingrese el valor de β: "))

# Listas para almacenar los datos
t = [0]
S = [S0]
I = [I0]
R = [R0]

# Cálculo de la propagación de la infección
for n in range(N):
    t.append(t[n] + h)
    S.append(S[n] - h * α * I[n] * S[n] / N)
    I.append(I[n] + h * (α * I[n] * S[n] / N - β * I[n]))
    R.append(R[n] + h * β * I[n])

# Graficar la propagación de la infección
plt.plot(t, S, label="Suceptible")
plt.plot(t, I, label="Infectado")
plt.plot(t, R, label="Recuperado")
plt.legend()
plt.title("Propagación de una infección")
plt.xlabel("Tiempo")
plt.ylabel("Población")
plt.grid()
plt.show()

# Animación de la propagación de la infección
fig = plt.figure()
ax = fig.gca()

def actualizar(i):
    ax.clear()
    ax.plot(t[:i], S[:i], '-', label="Suceptible")
    ax.plot(t[:i], I[:i], '-', label="Infectado")
    ax.plot(t[:i], R[:i], '-', label="Recuperado")
    ax.set_title("Propagación de una infección")
    ax.set_xlabel("Tiempo")
    ax.set_ylabel("Población")
    ax.grid(True)
    ax.plot(t[i], S[i], 'o', markersize=10, color='r')
    ax.plot(t[i], I[i], 'o', markersize=10, color='r')
    ax.plot(t[i], R[i], 'o', markersize=10, color='r')
    ax.legend()

ani = animation.FuncAnimation(fig, actualizar, range(0, N), interval=50)
HTML(ani.to_html5_video())
