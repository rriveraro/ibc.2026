# Devolución — Cuestionario 0

**Estudiante:** RIVERA, ROCIO BELEN
**Divergencia KL global:** 27.96

---

### Moneda

- Divergencia KL: 0.1532

**Tu respuesta:** [0.45, 0.45, 0.1]
> Como no tenemos información de si la moneda esta cargada o no, supongo igual probabilidad tanto para que salga el anverso como el reverso. Y le agrego una probabilidad menor al canto ya que puede ocurrir pero considero que es menos probable.

**Respuesta de referencia:** [0.48, 0.52, 2e-07]
> Una moneda normal tiene dos caras, por lo que la probabilidad de que salga Anverso o Reverso es aproximadamente 0.5 cada una. Una vez cada 5 millones de tiradas queda en el borde.

### Cajas

- Divergencia KL: 1.585

**Tu respuesta:** [0.3333, 0.3333, 0.3333, 0]
> Asigno la misma creencia a las 3 cajas ya que lo unico que se es que el regalo puede estar en alguna de las 3. Segun la consigna, SABEMOS que el regalo ESTA detras de una de ellas por lo que le asigno 0 a Otro lugar.

**Respuesta de referencia:** [0, 0, 1, 0]
> En este caso, por casualidad, el regalo se encontraba en la tercera caja (índice 2).

### Mentir

- Divergencia KL: 0

**Tu respuesta:** [0, 0, 1, 0, 0]
> No mentir seria no afirmar que se cuando no se (maxima incertidumbre) y no ocultar aquello que si se (dada la informacion disponible)

**Respuesta de referencia:** [0, 0, 1, 0, 0]
> Maximizar incertidumbre (entropía) dada la información disponible (restricciones) garantiza no mentir: decir que sabemos cuando no sabemos y decir que no sabemos cuando sí sabemos.

### Universos

- Divergencia KL: 0.8891

**Tu respuesta:** [0, 0.1667, 0.1667, 0.1667, 0, 0.1667, 0.1667, 0.1667, 0.1667]
> Segun el contexto del problema, la caja que abren no contiene el regalo por lo que las opciones 0 y 4 son improbables. Al resto les asignamos la misma probabilidad 1/6.

**Respuesta de referencia:** [0, 0.1667, 0.1667, 0, 0, 0.3333, 0, 0.3333, 0]
> La realidad causal podría tener cualquier distribución que tenga 0 en los casos imposibles (Abren=1 es imposible porque la caja 1 está reservada; Regalo=1,Abren=1 y Regalo=2,Abren=2 y Regalo=3,Abren=3 son imposibles porque no se abre la caja con el regalo).
En este caso particular la referencia propone una realidad causal subyacente que tiene la misma distribución que la predicción de máxima incertidumbre (entropía) dada la información disponible (restricciones).

### Historia

- Divergencia KL: 0.5146

**Tu respuesta:** [0, 0, 0.1, 0.7, 0.1, 0.1]
> Justifique

**Respuesta de referencia:** [0, 0, 0, 1, 0, 0]
> Según nuestro conocimiento, el primer uso fue en el siglo 18, por el señor Bayes.

### Conjunta

- Divergencia KL: 3.322

**Tu respuesta:** [0.1, 0.8, 0.1]
> (sin justificación)

**Respuesta de referencia:** [1, 0, 0]
> Por la regla de la cadena de la probabilidad, cualquier distribución conjunta siempre puede factorizarse de manera exacta como el producto de una marginal y la condicional del resto de variables dadas las anteriores. Es una identidad algebraica universal.

### Independencia

- Divergencia KL: 1.152

**Tu respuesta:** [0.45, 0.45, 0.1]
> Me confunde el enunciado ya que si A es independiente de B, P(A|B) = P(A). Luego, la igualidad es cierta siempre que se cumpla que A es independiente de B.

**Respuesta de referencia:** [1, 0, 0]
> Si A es independiente de B, se cumple también que P(B|A) = P(B) y por lo tanto siempre se cumple la igualdad dada en el enunciado.

### Descomposiciones

- Divergencia KL: 2.585

**Tu respuesta:** [0, 0, 0, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667, 0.1667]
> No se la respuesta por lo que distribuyo el total entre las 6 opciones que me parecieron viables.

**Respuesta de referencia:** [0, 0, 0, 0, 0, 0, 1, 0, 0]
> Cada permutación produce una factorización única utilizando la regla de la cadena, por lo que existen N! descomposiciones posibles.

### Teorema de Bayes

- Divergencia KL: 1.152

**Tu respuesta:** [0.45, 0.45, 0.1]
> Creeria que vale siempre ya que es lo que vine viendo desde Probabilidad y estastica y estadistica e inferencia, que es una constante de normalizacion y etc, pero no estoy cien por ciento segura.

**Respuesta de referencia:** [1, 0, 0]
> El denominador del Teorema de Bayes es la verosimilitud marginal, P(Datos), calculada integrando todo el espacio de hipótesis.
Debido a que la hipótesis no es un parámetro de esa función, siempre es constante para las diferentes hipótesis.

### Predicciones

- Divergencia KL: 3.322

**Tu respuesta:** [0.45, 0.45, 0.1]
> No estoy segura. Creeria que el orden no importa pero no lo se con certeza, es más una intuicion.

**Respuesta de referencia:** [0, 0, 1]
> Todas las descomposiciones generadas por la regla de la cadena son equivalentes y por lo tanto el orden temporal no juega ningún rol en el cálculo de la predicción conjunta.

### Valor de verdad

- Divergencia KL: 1.585

**Tu respuesta:** [0.3333, 0.3333, 0.3333]
> No sé la respuesta.

**Respuesta de referencia:** [1, 0, 0]
> Si una hipótesis asigna probabilidad nula a un dato que ha sido efectivamente observado, P(D|H)=0, por la regla de la cadena la predicción conjunta va a ser 0 siempre, P(Datos|H)=0, esa hipótesis se hace falsa para siempre, la creencia a posterior de esa hipótesis va a ser 0.

### Teorías causales

- Divergencia KL: 1.585

**Tu respuesta:** [0.3333, 0.3333, 0.3333, 0, 0]
> Justifique

**Respuesta de referencia:** [0, 0, 1, 0, 0]
> La predicción que el modelo hace de los datos, P(Datos|Modelo), en escala logarítmica y en tiempo infinito (ensamble o repeticiones del proceso) es precisamente el negativo de la entropía cruzada entre el proceso generativo de los datos P(Datos|Realidad) y las predicciones P(Datos|Modelo).
Sabemos que la entropía cruzada se minimiza cuando P(Datos|Modelo) = P(Datos|Realidad).

### Predicción e información

- Divergencia KL: 1.585

**Tu respuesta:** [0.3333, 0.3333, 0.3333]
> No sé

**Respuesta de referencia:** [0, 0, 1]
> Una predicción perfecta agrega nula información.
Cuanto mejor se predice, menos información se obtiene.
Siempre.
Nunca ocurre lo contrario.

### Modelos e información

- Divergencia KL: 1.585

**Tu respuesta:** [0.3333, 0.3333, 0.3333]
> Creo que al evaluar un modelo causal vamos a preferir ver otras cosas antes que la información de Shannon, pero no se.

**Respuesta de referencia:** [0, 0, 1]
> Queremos el modelo causal que predice perfectamente, que no recibe ningún tipo de información de Shannon.

### Evaluación de modelos

- Divergencia KL: 2

**Tu respuesta:** [0.5, 0.25, 0.25]
> Creo que tener suficientes datos es util, pero no sé con certeza.

**Respuesta de referencia:** [0, 1, 0]
> Es posible que dos modelos causales alternativos tengan la misma distribución conjunta.
En esos casos no podemos distinguir cuál es el modelo correcto, porque ambos hacen las mismas predicciones.

### Contrafactuales

- Divergencia KL: 1.585

**Tu respuesta:** [0.3333, 0.3333, 0.3333]
> No se

**Respuesta de referencia:** [1, 0, 0]
> Los contrafactuales siguen una lógica causal que puede incluirse en el modelo causal usando los mecanismos causales probabilísticos.
Ese modelo extendido contiene variables factuales y contrafactuales, y permite predecir cuál hubiera sido un resultado contrafactual dada la información factual.

### Diversificación

- Divergencia KL: 0.152

**Tu respuesta:** [0.01, 0.01, 0.01, 0.01, 0.01, 0.9, 0.01, 0.01, 0.01, 0.01, 0.01]
> Conviene no jugar, pero si no queda otra, apostar mitad y mitad.

**Respuesta de referencia:** [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
> El proceso de actualización de los recursos tiene una estructura multiplicativa.
La variable libre es la proporción de recursos que asignamos a Cara y Sello.
Los pagos que ofrece la casa de apuestas, en cambio, no cambian.
Al comparar el cociente entre dos riquezas generadas mediante dos estrategias de diversificación alternativas, los pagos de la casa de apuestas se cancelan.
La ecuación a optimizar es la media geométrica de la diversificación dada la probabilidad de la moneda.
En escala logarítmica tiene la estructura de la entropía cruzada, con el signo invertido.
Y eso se maximiza cuando la diversificación es igual a la probabilidad de la moneda.

### Apuesta individual

- Divergencia KL: 0.152

**Tu respuesta:** [0.9, 0.1]
> Conviene no jugar.

**Respuesta de referencia:** [1, 0]
> Aunque la esperanza aritmética es positiva, lo que importa individualmente es la tasa de crecimiento geométrica: (1.5)^0.5 * (0.6)^0.5 = sqrt(1.5 * 0.6) = sqrt(0.9) ≈ 0.9487 < 1.
La riqueza típica decrece ~5.1% por jugada.

### Teoría de Utilidad Esperada

- Divergencia KL: 1.152

**Tu respuesta:** [0.1, 0.45, 0.45]
> No creo que convenga jugar igual.

**Respuesta de referencia:** [0, 0, 1]
> A pesar de que la esperanza de los recursos es positiva, la tasa de crecimiento de la riqueza a largo plazo es negativa.
Esto se puede ver en dos pasos, con un Sello y una Cara.
Cuando sale Sello pasamos de 100 a 60, y luego cuando sale Cara pasamos de 60 a 90.
Y como la moneda es normal, a largo plazo vamos a tener la misma cantidad de Caras y Sellos, y la riqueza decrece siempre.

### Fondo común

- Divergencia KL: 0.3219

**Tu respuesta:** [0.1, 0.1, 0.8]
> Justifique

**Respuesta de referencia:** [0, 0, 1]
> Al poner los recursos en un fondo común y dividirlo en partes iguales, la tasa de crecimiento aumenta para todos los participantes.
A medida que el grupo es más grande, la tasa de crecimiento se parece más a la media aritmética, que es positiva, por lo que Sí conviene participar.

### Impuestos

- Divergencia KL: 1.585

**Tu respuesta:** [0.3333, 0.3333, 0.3333]
> No sé

**Respuesta de referencia:** [1, 0, 0]
> Cuando dejamos de aportar al fondo común se reduce la tasa de crecimiento del grupo del cual dependemos y con ella cae nuestra tasa de crecimiento.
Esto se observa matemática y numéricamente.

## Resumen

- **Divergencia KL global:** 27.96
- **Preguntas con divergencia KL infinita** (asignaste 0 a una opción con probabilidad de referencia positiva): 0 de 21
- **Preguntas sin distribución de creencias válida** (reemplazadas por máxima incertidumbre): 0 de 21