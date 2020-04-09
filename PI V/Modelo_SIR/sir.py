from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
# População total, N.
N = 15000
# Número inicial de indivíduos infectados e recuperados, I0 e R0.
I0, R0 = 1, 0
# Todos os outros, S0, são suscetíveis à infeção inicialmente.
S0 = N - I0 - R0
# Taxa de infecção, beta, e taxa média de recuperação, gamma, (em 1/dias.
beta, gama = 0.0001, 1/10
# Quantidade de pontos que queremos monitorar (dias)
eventos = range(0, 61)
# Quantidade de pontos a integrar (intervalo de integração)
pontos = [0, 1001]

def deriv(t, y, N, beta, gama):
    S, I, R = y
    dSdt = -beta * S * I
    dIdt = beta * S * I - gama * I
    dRdt = gama * I
    return dSdt, dIdt, dRdt
# Vetor de condições iniciais
y0 = S0, I0, R0
# Integração das equações do modelo pela grade de tempo, t.
sol = solve_ivp(deriv, pontos, y0, args=(N, beta, gama), t_eval=eventos,
                method='RK23')

#Plota os dados em quatro curvas diferentes para S(t), I(t), R(t) e D(t)
graf = plt.figure(facecolor='w')
plt.xlabel('Tempo /dias')
plt.ylabel('Indivíduos')
plt.plot(sol.t, sol.y[0], 'b', label='Suscetíveis')
plt.plot(sol.t, sol.y[1], 'r', label='Infectados')
plt.plot(sol.t, sol.y[2], 'g', label='Recuperados com imunidade')
plt.legend()
plt.show()

graf.savefig('grafico.png')
