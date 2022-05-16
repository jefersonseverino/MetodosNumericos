import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def dAdt(A, t, beta, gamma, N, nu, alpha, eta):
    #definindo as variáveis.
    S = A[0]
    E = A[1]
    I = A[2]
    R = A[3]
    D = A[4]
    V = A[5]
    return [
        -beta/N * S * I - v*S,
        beta/N * S * I - alpha * E,
        alpha * E - gamma * I,
        gamma * (1 - eta) * I,
        gamma * eta * I,
        v*S
    ]

#Quanto tempo será simulado
times = np.arange(0, 500, 1)

#definindo os valores das constantes
gamma = 0.083
N = 1e7
beta = 0.20
v = 0.04
alpha = 0.192
eta = 0.024

#Valores iniciais das variáveis
S0, E0, I0, R0, D0, V0 = N-800, 800, 0, 0, 0, 0

#resolvendo a ODE.
sol = odeint(dAdt, y0=[S0, E0, I0, R0, D0, V0],t=times, args=(beta, gamma, N, v, alpha, eta))

#plotando os gráficos.
S = sol.T[0]
E = sol.T[1]
I = sol.T[2]
R = sol.T[3]
D = sol.T[4]
V = sol.T[5]

plt.figure(facecolor='w',figsize=(30,10))
plt.plot(times, S)
plt.plot(times, E)
plt.plot(times, I)
plt.plot(times, R)
plt.plot(times, D)
plt.plot(times, V)

plt.grid()
plt.show()

