import argparse
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def simulate_infection(N, alpha, beta, S0, I0, R0):
    h = 25 / (N - 1)
    t = [0]
    S = [S0]
    I = [I0]
    R = [R0]

    for n in range(N):
        t.append(t[n] + h)
        S.append(S[n] - h * alpha * I[n] * S[n])
        I.append(I[n] + h * (alpha * I[n] * S[n] - beta * I[n]))
        R.append(R[n] + h * beta * I[n])

    return t, S, I, R

def update_plot(frame, t, S, I, R, line1, line2, line3, line4):
    line1.set_data(t[:frame], S[:frame])
    line2.set_data(t[:frame], I[:frame])
    line3.set_data(t[:frame], R[:frame])
    line4.set_data(t[frame], S[frame])
    line4.set_data(t[frame], I[frame])
    line4.set_data(t[frame], R[frame])
    return line1, line2, line3, line4


def main():
    parser = argparse.ArgumentParser(description="Simulación de propagación de una infección")
    parser.add_argument("--N", type=int, default=1000, help="Número de iteraciones")
    parser.add_argument("--alpha", type=float, default=0.0014, help="Tasa de infección")
    parser.add_argument("--beta", type=float, default=0.6, help="Tasa de recuperación")
    parser.add_argument("--S0", type=int, default=995, help="Población suceptible inicial")
    parser.add_argument("--I0", type=int, default=5, help="Población infectada inicial")
    parser.add_argument("--R0", type=int, default=0, help="Población recuperada inicial")
    args = parser.parse_args()

    t, S, I, R = simulate_infection(args.N, args.alpha, args.beta, args.S0, args.I0, args.R0)

    fig, ax = plt.subplots()
    line1, = ax.plot([], [], label="Suceptible")
    line2, = ax.plot([], [], label="Infectado")
    line3, = ax.plot([], [], label="Recuperado")
    line4, = ax.plot([], [], 'ro', markersize=10, color='r')
    line5, = ax.plot([], [], 'ro', markersize=10, color='r')
    line6, = ax.plot([], [], 'ro', markersize=10, color='r')

    ax.set_title("Propagación de una infección", fontweight="bold", size=20)
    ax.set_xlabel("Tiempo", fontweight="bold", size=15)
    ax.grid(True)
    ax.legend()

    anim = FuncAnimation(fig, update_plot, frames=args.N, fargs=(t, S, I, R, line1, line2, line3, line4), interval=50, blit=True)

    plt.show()

if __name__ == "__main__":
    main()
