"""
Práctica 1.1: Argumentos causales alternativos e incertidumbre.
============================================
"""

import warnings
from typing import List, Tuple

import matplotlib.pyplot as plt
import numpy as np

warnings.filterwarnings("ignore")

# ------------------------------------------------------------
# 1. Definición del espacio de hipótesis
# ------------------------------------------------------------

# H representa las 3 cajas posibles {0, 1, 2}
H = np.arange(3)


# ------------------------------------------------------------
# 2. Priors
# ------------------------------------------------------------


def p_r(r: int) -> float:
    """
    P(R = r).
    Prior sobre la ubicación del regalo.
    r ∈ {0, 1, 2}
    """
    prob = [1/3, 1/3, 1/3]
    if r in [0,1,2]:
        return prob[r]
    else:
        return "Posición incorrecta, prueba con un numero entre 0 y 2"


def p_c(c: int) -> float:
    """
    P(C = c).
    Prior sobre la caja elegida por el participante
    c ∈ {0, 1, 2}
    """
    prob = [1/3, 1/3, 1/3]
    if c in [0,1,2]:
            return prob[c]
    else:
            return "Posición incorrecta, prueba con un numero entre 0 y 2"


# ------------------------------------------------------------
# 3. Modelos del presentador
# ------------------------------------------------------------


def p_s_rM0(s: int, r: int) -> float:
    """
    P(S = s | R= r, M = 0).
    Modelo 0 (No Monty Hall):
    El presentador abre cualquier caja que no tenga el regalo.
    s ∈ {0, 1, 2}
    r ∈ {0, 1, 2}
    """
    #s serian las columnas
    #r serian las filas
    prob = [
    [0, 0.5, 0.5],  
    [0.5, 0, 0.5], 
    [0.5, 0.5, 0]]

    if s in [0,1,2]:
        if r in [0,1,2]:
            return prob[r][s]
        else:
                return "Posición incorrecta, prueba con un numero entre 0 y 2"
    else:
        return "Posición incorrecta, prueba con un numero entre 0 y 2"


def p_s_rcM1(s: int, r: int, c: int):
    """
    P(S = s | R= r, C= c, M = 1).
    Modelo 1 (Monty Hall):
    El presentador abre una caja que no tenga el regalo
    ni haya sido seleccionada.
    s ∈ {0, 1, 2}
    r ∈ {0, 1, 2}
    c ∈ {0, 1, 2}
    """
    prob={
         0 : [[0, 0.5, 0.5],[0, 0, 1],[0, 1, 0]],
         1 : [[0, 0, 1],[0.5, 0, 0.5],[1, 0, 0]],
         2 : [[0,1,0],[1,0,0],[0.5,0.5,0]]
    }
    if c in [0,1,2]:
        if r in [0,1,2]:
              if s in [0,1,2]:
                   return prob[c][r][s]
              else:
                      return "Posición incorrecta, prueba con un numero entre 0 y 2"
        else:
                return "Posición incorrecta, prueba con un numero entre 0 y 2"
    else:
            return "Posición incorrecta, prueba con un numero entre 0 y 2"
        

# ------------------------------------------------------------
# 4. Distribución conjunta P(r, c, s | M)
# ------------------------------------------------------------


def p_rcs_M(r: int, c: int, s: int, m: int) -> float:
    """
    P(r, c, s | M) = P(r | M)P(c | M)P(s | r, c, M)
    Distribución conjunta del modelo m.
    s ∈ {0, 1, 2}
    r ∈ {0, 1, 2}
    c ∈ {0, 1, 2}
    m ∈ {0, 1}
    """
    if m in [0,1]:
         if m==0:
              return p_r(r)*p_c(c)*p_s_rM0(s)
         elif m==1:
                       return p_r(r)*p_c(c)*p_s_rcM1(s)
    else:
         return "Posición incorrecta, prueba con un numero entre 0 y 1"


# ------------------------------------------------------------
# 5. Simulación de datos (asumiendo Monty Hall verdadero)
# ------------------------------------------------------------

np.random.seed(42)


def simular(T=16) -> List[Tuple[int, int, int]]:
    """
    Función para simular datos según el modelo Monty Hall verdadero.
    T: número de datos a generar.
    """
    p_r_probs = [p_r(r) for r in H]
    p_c_probs = [p_r(c) for c in H]

    lista=[]

    for _ in range(T):
         ct = np.random.choice(H,p_c_probs)
         rt = np.random.choice(H,p_r_probs)

         p_s_probs = [p_s_rcM1(s, rt, ct) for s in H]
         st = np.random.choice(H,p_s_probs)
         tup=(ct ,st ,rt)
         lista.append(tup)

    return lista



# ------------------------------------------------------------
# 6. Probabilidad de los datos dado un modelo
# ------------------------------------------------------------



def p_r_sM0(s,r):
    if s == r:
        return 0
    if s in H and r in H:
        return 0.5
    else:
         "Error, ingrese un numero valido"
    
def p_r_scM1(s,c,r):
    if s == r or s == c:
        return 0
    if r == c:
        # El participante eligió la del regalo. Hay 2 opciones restantes válidas (1/2 cada una).
        return 0.5
    else:
        # El participante eligió una caja vacía. Hay solo 1 opción restante válida (probabilidad 1.0).
        return 1

def pEpisodio_M(c,s,r,m):
     '''
     Implementar la predicci ́on que el modelo hace de un episodio 
     P (ct, st, rt | M ) =P (ct |M ) P (st |ct, M ) P (rt |st, ct, M )
     pEpisodio M(c,s,r,m)
     '''
     if m==0:
        return p_c(c)*p_s_rM0(s)*p_r_sM0(s,r)  #P (ct |M ) P (st |ct, M ) P (rt |st, ct, M )
     elif m==1:
        return p_c(c)*p_s_rM0(s)*p_r_scM1(s,c,r)  #P (ct |M ) P (st |ct, M ) P (rt |st, ct, M )
     else:
          return "Error"

import math
def pDatos_M(datos: List[Tuple[int, int, int]], m: int) -> float:
    """
    P(Datos | M) = prod([ P(c,s,r|M) for c, s, r in Datos ])
    Probabilidad de ver los datos dados el modelo considerado.
    m ∈ {0, 1}
    """
    lista=[]
    for c,s,r in datos:
        aux=pEpisodio_M(c,s,r,m)
        lista.append(aux)
    return math.prod(lista)


# ------------------------------------------------------------
# 7. Probabilidad total de ver los datos
# ------------------------------------------------------------


def pM(m: int) -> float:
    """
    P(M)
    Prior sobre los modelos.
    m ∈ {0, 1}
    """
    pass


def pDatos(datos: List[Tuple[int, int, int]]) -> float:
    """
    P(Datos)
    Probabilidad total de ver los datos usando la contribución
    de todos los modelos.
    """
    pass


# ------------------------------------------------------------
# 8. Actualización de creencias sobre los modelos
# ------------------------------------------------------------


def pM_Datos(m: int, datos: List[Tuple[int, int, int]]) -> float:
    """
    P(M | Datos)
    Actualización de la creencia sobre el modelo M dado los datos
    (distribución a posteriori).
    """
    pass


def evolucion_posterior(m: int, datos: List[Tuple[int, int, int]]) -> List[float]:
    """
    Evolución del posterior de los modelos según se observa información.
    """
    pass



# ------------------------------------------------------------
# 9. Cálculo del bayes factor
# (diferencia en órdenes de magnitud en escala logarítmica)
# ------------------------------------------------------------


def log_pDatos_M(datos: List[Tuple[int, int, int]], m: int) -> float:
    """
    log(P(Datos | M))
    Logaritmo de la probabilidad de ver los datos dados el modelo considerado.
    """
    pass


def log_bayes_factor(datos: List[Tuple[int, int, int]], m_i: int, m_j: int) -> float:
    """
    log(Datos | Mi / Datos | Mj) = log_10P(Datos | Mi) - log_10P(Datos | Mj)
    Bayes factor en escala logarítmica para comparar dos modelos.
    m_i, m_j ∈ {0, 1}
    """
    pass


# ------------------------------------------------------------
# 10. Predicción típica que realizan los modelos sobre los datos
# ------------------------------------------------------------

def prediccion_tipica(datos: List[Tuple[int, int, int]], m: int) -> float:
    """
    log(Media Geométrica)
    Logaritmo de la media geométrica de los datos dados el modelo considerado.
    m ∈ {0, 1}
    """
    pass



# ------------------------------------------------------------
# 11. Ejecución principal
# ------------------------------------------------------------

if __name__ == "__main__":
    # Simulación
    datos = simular(T=16)

    # Print de funciones
    print("log_bayes_factor (M1 contra M0):", log_bayes_factor(datos, 1, 0))
    print("prediccion_tipica (M0):", prediccion_tipica(datos, 0))
    print("prediccion_tipica (M1):", prediccion_tipica(datos, 1))

    # Posteriores
    post_M0 = evolucion_posterior(0, datos)
    post_M1 = evolucion_posterior(1, datos)

    # Gráfico
    plt.figure(figsize=(8, 6))
    plt.plot(post_M0, label="M0: Base")
    plt.plot(post_M1, label="M1: Monty Hall")
    plt.xlabel("Número de episodios")
    plt.ylabel("P(Modelo | Datos)")
    plt.title("Evolución del posterior de los modelos")
    plt.legend()
    plt.tight_layout()
    plt.show()
