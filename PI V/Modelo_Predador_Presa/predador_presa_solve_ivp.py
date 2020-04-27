import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

#taxa de crescimento dos coelhos sem predador
alfa = 1.0

#chance da raposa encontrar e comer o coelho
beta = 0.1

#taxa de crescimento das raposas com alimento
gama = 0.75

#taxa de morte por inanição
delta = 1.5

#Sistema de equações diferenciais
def deriv(t, P):
    c, r = P
    dcdt = alfa * c - beta * c * r
    drdt = gama * r * beta *c - delta * r
    return dcdt, drdt

# Quantidade de eventos que queremos monitorar (18 meses)
eventos = range(0, 18)
# Quantidade de pontos a integrar (intervalo de integração)
pontos = [0, 1001]

#população inicial de 10 coelhos e 5 raposas
P0 = [10, 5]

#Computa a solução do sistema de equações diferenciais
sol = solve_ivp(deriv, pontos, P0, t_eval=eventos, 
                method='RK45')

coelhos = sol.y[0]
raposas = sol.y[1]

plt.plot(sol.t, coelhos, "r", label="Coelhos")
plt.plot(sol.t, raposas, "b", label="Raposas")
plt.xlabel("Tempo (meses)")
plt.ylabel("População")
plt.legend();
plt.show()
