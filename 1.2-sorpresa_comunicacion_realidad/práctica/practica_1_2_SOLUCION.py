from matplotlib import pyplot as plt
import numpy as np
from numpy import nan
import math

# Hipótesis (posibles valores)
h = np.arange(3)

#
# 1.1 Definir la distribución de creencia conjunta como producto de las distribuciones condicionales del modelo .
#

# Probabilidad del modelo
def pM(m): # P(m)
    return 1/2

# Probabilidad del regalo
def pr(r): # P(r)
    return 1/3

# Probabilidad de cerrar
def pc(c): # P(c)
    return 1/3

# Probabilidad de la pista modelo Base M0
def ps_rM0(s,r):
    return (s != r) * 1/2

# Probabilidad de la pista modelo Monty Hall M1
def ps_rcM1(s,r,c):
    if r != c:
        return (s != r) * (s != c) * 1
    else:
        return (s != r) * 1/2

# Predicción del episodio
def pcsr_M(c,s,r,m):
    if m == 0:
        return pr(r) * pc(c) * ps_rM0(s, r)
    if m == 1:
        return pr(r) * pc(c) * ps_rcM1(s, r, c)

#
# Simular datos con el modelo Monty Hall
#
def simular(T = 16, seed = 0):
    np.random.seed(seed) # Para que los números aleatorios sean siempre iguales
    Datos = [] # La lista de los datos
    for t in range(T): # Itero por episodio
        # Genero los datos del episodio
        r = np.random.choice(3, p=[pr(hr) for hr in h ])
        c = np.random.choice(3, p=[pc(hc) for hc in h ])
        s = np.random.choice(3, p=[ps_rcM1(hs, r, c) for hs in h])
        Datos.append((c,s,r)) # Agrega el episodio como una tupla (c,s,r)
    return Datos

T = 16
Datos = simular(T)

#
# Calcular la predicción a priori que hace cada uno de los modelos sobre la totalidad de la base de datos simulada
#

def pDatos_M(Datos,m):
    # Inicializacion de la secuencia de predicciones de los modelos
    res = [1]
    for t in range(len(Datos)): # Itero sobre episodios
        c, s, r = Datos[t]
        # Predicciones
        # P(r,c,s|M) = P(r)P(c)P(s|r,c)
        res.append(  pcsr_M(c,s,r,m) )
    return np.array(res)

#
# La predicción del modelo expresada en órdenes de magnitud
#

pDatos_M0 = pDatos_M(Datos,0)
pDatos_M1 = pDatos_M(Datos,1)
log_evidencia_M0 = np.sum(np.log10(pDatos_M0))
log_evidencia_M1 = np.sum(np.log10(pDatos_M1))

print("Diferencia de desempeño predictivo expresado en órdenes de magnitud =", log_evidencia_M1-log_evidencia_M0)
print("La cantidad creencia que preservó el modelo Monty Hall respecto del modelo Base =", 10**(log_evidencia_M1-log_evidencia_M0))

#
# La predicción típica (o media geométrica)
#

log_evidencia_M0 = np.sum(np.log10(pDatos_M0))
log_evidencia_M1 = np.sum(np.log10(pDatos_M1))
print("Predicción típica del modelo Base (M0) =", 10**(log_evidencia_M0/(T*3)) )
print("Predicción típica del modelo Monty Hall (M1) =", 10**(log_evidencia_M1/(T*3)) )


# P(Datos, Modelo) = P(Datos|Modelo) P(Modelos)
pDatosM = [np.cumprod(pDatos_M0) * pM(0),
           np.cumprod(pDatos_M1) * pM(1)]
pDatos = pDatosM[0] + pDatosM[1]

# P(Modelo = m | Datos = {(c1,s1,r1),...,(ct,st,rt)} ) = pM_Datos[m][t]
pM_Datos = [pDatosM[0] / pDatos,
            pDatosM[1] / pDatos]

plt.plot(pM_Datos[0] , label="M0: Base")
plt.plot(pM_Datos[1] , label="M1: Monty Hall")
plt.xlabel("Episodio")
plt.ylabel("P( Modelo | Datos )")
plt.legend(title="Realidad causal: Monty Hall \n \nProbabilidad de los modelos:")
#plt.show()
plt.close()


#
# Datos NoMontyHall
#


def NoMontyHall(T = 16, seed = 0):
    np.random.seed(seed) # Para que los números aleatorios sean siempre iguales
    Datos = [] # La lista de los datos
    for t in range(T): # Itero por episodio
        # Genero los datos del episodio
        r = np.random.choice(3, p=[pr(hr) for hr in h ])
        c = np.random.choice(3, p=[pc(hc) for hc in h ])
        m = np.random.choice(2, p=[1/4, 3/4])
        s = np.random.choice(3, p=[ps_rM0(hs,r) if m==0 else ps_rcM1(hs, r, c) for hs in h])
        Datos.append((c,s,r)) # Agrega el episodio como una tupla (c,s,r)
    return Datos


DatosNoMontyHall = NoMontyHall(2000)
pDatosNoMontyHall_M0 = pDatos_M(DatosNoMontyHall,0 )
pDatosNoMontyHall_M1 = pDatos_M(DatosNoMontyHall,1 )

# ------------------------------------------------------------
# 3. Priors sobre la memoria p y la probabilidad de acordarse a
# ------------------------------------------------------------

# Hipótesis de memoria
P_GRID = np.arange(0,1.05,0.05) # P_GRID

# Pisamos el prior de los modelos, ahora tenemos 3.
def pM(m): # P(m)
    return 1/3

def pp(p):
    # P(p)
    return 1/len(P_GRID)

def pa_p(a, p):
    #P(a|p)
    if a == 1:
        return p
    if a == 0:
        return 1-p

def ps_rcaM2(s,r,c,a):
    # El mecanismo causal que tiene una gate
    # cambia el mecanismo en función del
    # contexto (si se acuerda o no)
    if a == 0:
        return ps_rM0(s,r)
    if a == 1:
        return ps_rcM1(s,r,c)

def prcs_DatosM2(r,c,s,pp_Datos):
    # P(r,c,s|Datos,M2)
    # Predicción de un episodio dado los episodios anteriores
    # En vez de recibir Datos como variable, recibe el último
    # posterior de la memoria, que usa como prior para el
    # siguiente evento.
    # pp_Datos es una lista con el último posterior de p
    #
    # A diferencia de la predicción que hacen los otros modelos
    # este debe integrar las variables ocultas a y p.
    # P(r,c,s|Datos,M2) = \sum_{a,p} P(r)P(c)P(s|r,c,a)P(a|p)P(p|Datos)
    res = 0
    for a in [0,1]:
        for i_p in range(len(P_GRID)):
            p = P_GRID[i_p]
            res += pr(r)*pc(c)*ps_rcaM2(s,r,c,a)*pa_p(a,p)*pp_Datos[i_p]
    return res



def prcs_pM2(r,c,s,p):
    # Likelihhod P(r,c,s|p,M2)
    # P(r,c,s|p,M2) = \sum_{a} P(r)P(c)P(s|r,c,a)P(a|p)
    res = 0
    for a in [0,1]:
        res += pr(r)*pc(c)*ps_rcaM2(s,r,c,a)*pa_p(a,p)
    return res


def pDatos_M(Datos,m):
    # P(Datos|M), la re-escribimos agregando el 3er modelo.
    #
    # Vamos a devolver una lista con todas las predicciones
    res = [1]
    #
    # Inicializamos una lista con el prior de p
    pp_Datos = np.array([pp(p) for p in P_GRID])
    for t in range(len(Datos)):
        c, s, r = Datos[t]
        if m == 0 or m == 1:
            res.append(  pcsr_M(c,s,r,m) )
        if m == 2:
            # Predecimos usando el último pp_Datos
            prediccion = prcs_DatosM2(r,c,s,pp_Datos)
            res.append(float(prediccion))
            # Actualizamos el posterior de p, pp_Datos
            likelihhod = [prcs_pM2(r,c,s,p) for p in P_GRID]
            pp_Datos = pp_Datos * likelihhod
            pp_Datos = pp_Datos / sum(pp_Datos)
    return np.cumprod(res)


# P(Datos,M) el posterior proporcional (\propto P(M|Datos))
def pDatosM(Datos, m):
    return pDatos_M(Datos, m)*pM(m)


# P(Datos)
def pDatos(Datos):
    return pDatosM(Datos,0)+pDatosM(Datos,1)+pDatosM(Datos,2)


# P(Modelo = m | Datos = {(c1,s1,r1),...,(ct,st,rt)} )
def pModelo_Datos(m,Datos):
    return pDatosM(Datos,m)/pDatos(Datos)

plt.plot(pModelo_Datos(0,DatosNoMontyHall)[0:100], label="M0: Base")
plt.plot(pModelo_Datos(1,DatosNoMontyHall)[0:100], label="M1: Monty Hall")
plt.plot(pModelo_Datos(2,DatosNoMontyHall)[0:100], label="M2: Alternativo")
plt.xlabel("Episodio")
plt.ylabel("P( Modelo | Datos )")
plt.legend(title="Realidad causal: No Monty Hall \n \nProbabilidad de los modelos:")
plt.show()

