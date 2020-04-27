import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#taxa de crescimento dos coelhos sem predador
alfa = 1.0

#chance da raposa encontrar e comer o coelho
beta = 0.1

#taxa de crescimento das raposas com alimento
gama = 0.75

#taxa de morte por inanição
delta = 1.5

#Sistema de equações diferenciais
def deriv(P, t):
    c, r = P
    dcdt = alfa * c - beta * c * r
    drdt = gama * r * beta *c - delta * r
    return dcdt, drdt

#intervalo de integração (18 meses com 1000 pontos)
t = np.linspace(0, 18, 1000)

#população inicial de 10 coelhos e 5 raposas
P0 = [10, 5]

#Computa a solução do sistema de equações diferenciais
sol = odeint(deriv, P0, t)

coelhos = sol[:,0]
raposas = sol[:,1]

plt.plot(t, coelhos, "r", label="Coelhos")
plt.plot(t, raposas, "b", label="Raposas")
plt.xlabel("Tempo (meses)")
plt.ylabel("População")
plt.legend();
plt.show()
