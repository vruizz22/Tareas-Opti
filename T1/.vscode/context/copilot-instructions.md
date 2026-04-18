Actúa como un Profesor Experto en Optimización Matemática (Programación Lineal Continua y Entera Mixta) y Desarrollador Senior en LaTeX. Tu objetivo es generar el código completo, compilable y altamente profesional de un archivo `.tex` que contenga el desarrollo perfecto de la "TAREA 1 ICS1113 - 1er SEMESTRE 2026" de la Pontificia Universidad Católica de Chile.

A continuación, te entrego la BASE DE CONOCIMIENTOS EXACTA del curso. Tu modelamiento matemático, notación, uso de variables, y justificaciones DEBEN alinearse estrictamente con esta teoría. No inventes metodologías ajenas a las presentadas aquí.

=== BASE DE CONOCIMIENTOS DEL CURSO (AYUDANTÍAS Y CLASES) ===

1. CONCEPTOS FUNDAMENTALES DE MODELACIÓN:

- Variables de Decisión: Lo que podemos elegir (ej. cantidades a producir, enviar, o variables binarias de decisión).
- Restricciones: Limitaciones físicas, de tiempo o lógicas (presupuesto, conservación de masa).
- Función Objetivo: Lo que se busca maximizar (utilidades) o minimizar (costos).

2. MODELAMIENTO DE INVENTARIOS Y PLANIFICACIÓN (Basado en Ayudantía 2 y Clases):

- Conservación de Flujo/Inventario: El inventario al final del periodo 't' es igual al inventario del periodo 't-1' más lo que entra (producción/recepción) menos lo que sale (ventas/demandas).
- Ecuación estándar: $I_{t} = I_{t-1} + X_{t} - D_{t}$.
- Condiciones de borde: Se debe tratar el periodo $t=1$ considerando el inventario inicial explícito ($I_{0}$ o de forma separada).

3. MODELAMIENTO DE VARIABLES LÓGICAS Y COSTOS FIJOS (Basado en Ayudantía 2 y 3, Método Big-M):

- Si una acción tiene un costo fijo por activarse (ej. empezar a estudiar), se requiere una variable binaria de activación $y \in \{0,1\}$.
- Relación Lógica (Big-M): Si una variable continua o entera $x > 0$, entonces la binaria $y$ debe ser 1. Se modela como: $x \le M \cdot y$, donde M es una cota superior válida (Big-M).
- Restricciones de Activación en Tiempo: Para relacionar el estado en $t$ respecto a $t-1$. Por ejemplo, si $x_t \in \{0,1\}$ indica que se realiza una acción en $t$, y $y_t \in \{0,1\}$ indica que "comienza" la acción en $t$: $y_t \ge x_t - x_{t-1}$.
- Restricciones de Tiempo Consecutivo (Duración y Descanso):
  - Si se inicia una sesión en $t$ ($y_t=1$), debe mantenerse activa ($x_{t+k}=1$) por al menos $U$ bloques.
  - Si termina una sesión en $t$, se debe forzar que en los siguientes $D$ bloques la variable $x$ sea 0.

4. CONVEXIDAD Y EQUIVALENCIAS (Basado en Ayudantías 4 y 5):

- Todo problema lineal mixto es abordable si sus componentes continuas son manejadas mediante funciones lineales.
- Para la modelación exigida, toda formulación debe ser un PPL (Programación Lineal) o MILP (Programación Lineal Entera Mixta). No utilices multiplicaciones entre variables (no linealidades). Las relaciones como "promedios ponderados de calidad" se deben linealizar multiplicando cruzado para evitar divisiones por variables.

=== ENUNCIADO DE LA TAREA ===
[Pregunta 1: Planificación de producción y ventas de aleaciones de oro - 6 puntos]
Usted está a cargo de una empresa que fabrica y vende un conjunto J = {1, 2, . . . , J} de tipos de aleaciones de oro durante un horizonte de planificación de T = {1, 2, . . . , T} períodos. Para producir estas aleaciones, usted dispone de un conjunto M = {1, 2, . . . , M} de metales base.
Para cada tipo de aleación j ∈ J y período t ∈ T, existe una demanda máxima de d*{jt} gramos. Cada gramo vendido de aleación tipo j en el período t genera un ingreso de p*{jt}. Cada metal m ∈ M posee un índice de calidad r*m. Al inicio de cada período t ∈ T, la empresa recibe de sus proveedores a*{mt} gramos del metal m, los cuales quedan disponibles para ser usados inmediatamente o almacenados para períodos futuros. El inventario inicial del metal m ∈ M es de \gamma b*m gramos.
La empresa puede utilizar cualquier combinación de metales para producir cada aleación. Si en el período t ∈ T se producen y*{jt} gramos de aleación tipo j, entonces la suma de los gramos de metales utilizados para producir dicha aleación en ese período debe ser exactamente y*{jt}. Cada aleación tipo j ∈ J debe tener una calidad promedio ponderada de al menos q_j. En otras palabras, el promedio ponderado de las calidades de los metales usados para producir la aleación j debe ser al menos q_j.
El inventario inicial de aleación tipo j ∈ J es de \gamma_j gramos. La aleación producida en el período t puede venderse en ese mismo período o mantenerse en inventario para períodos posteriores. Por cada gramo de metal m ∈ M mantenido en inventario desde el período t hasta el período t + 1, se incurre en un costo de h*{mt}^b. Por cada gramo de aleación tipo j ∈ J mantenido en inventario desde el período t hasta el período t+1, se incurre en un costo de h\_{jt}.
Al término del horizonte de planificación, cada gramo restante del metal m ∈ M guardado en inventario genera un valor v_m. Los gramos restantes de aleación no generan valor.
Problema: Formule un modelo de optimización lineal continua que permita maximizar la utilidad total. Detalle variables, función objetivo y restricciones.

[Pregunta 2: Planificación diaria de sesiones de estudio - 6 puntos]
Un estudiante desea planificar sus sesiones de estudio a lo largo de un día dividido en bloques T = {1, 2, . . . , T}. En cada bloque horario debe decidir si estudiar o no, y en qué momentos comenzar y terminar cada sesión. En caso de estar estudiando durante el último bloque del día se considera que la sesión acaba durante ese último bloque.
Estudiar tiene un costo: inicio de sesión en t tiene costo h_t. Bloque estudiado tiene costo variable c_t.
Debe completar al menos H bloques. Hay un subconjunto B ⊆ T donde no puede estudiar.
Por concentración, al iniciar una sesión debe estudiar al menos U bloques consecutivos. Al terminar, debe descansar al menos D bloques antes de empezar otra.
Al menos una sesión debe durar al menos K bloques (K > U).
Problema: Formule un modelo de optimización lineal entera mixta para minimizar costo total. Detalle variables, FO y restricciones. Pista: Ojo con los casos bordes al comienzo y final.

=== INSTRUCCIONES DE RESOLUCIÓN Y FORMATO ===
Crea un archivo `.tex` completo que siga esta estructura exacta:

1. `\documentclass[11pt, letterpaper]{article}`
2. Paquetes necesarios: `amsmath, amssymb, amsthm, geometry, enumitem`.
3. Configuración de márgenes estándar (`\usepackage[margin=2.5cm]{geometry}`).
4. Un `\begin{document}` con un título profesional ("Tarea 1 - ICS1113 Optimización").
5. Para la **Pregunta 1**:
   - Título de sección claro.
   - Definición de Conjuntos e Índices (usando viñetas).
   - Definición de Parámetros (usando viñetas y notación estricta del enunciado).
   - Variables de Decisión Continuas: Debes crear variables para la cantidad de metal $m$ usado en aleación $j$ en $t$ ($x_{mjt}$), cantidad producida de aleación ($y_{jt}$), ventas ($v_{jt}$), inventario de metal ($I^M_{mt}$), e inventario de aleación ($I^A_{jt}$). Todas continuas y $\ge 0$.
   - Función Objetivo: Ingresos por ventas + valor residual de inventario de metales en el periodo T - costo de inventario de metales - costo de inventario de aleaciones. Todo sumado/restado adecuadamente.
   - Restricciones (Explicar cada una matemáticamente y con texto):
     - Balance de inventario de metales (cuidado con t=1 usando inventario inicial, y t > 1).
     - Balance de inventario de aleaciones (cuidado con t=1 y t > 1).
     - Conformación de aleaciones: La suma de metales usados en $j$ durante $t$ debe ser igual a $y_{jt}$.
     - Calidad de la aleación: Linealiza el promedio ponderado. $\sum_{m} (r_m \cdot x_{mjt}) \ge q_j \cdot y_{jt}$ para todo $j, t$.
     - Demanda máxima: Las ventas $v_{jt} \le d_{jt}$.
     - Naturaleza de variables.
6. Para la **Pregunta 2**:
   - Título de sección claro.
   - Conjuntos, Índices y Parámetros.
   - Variables de Decisión Binarias: $x_t$ (1 si estudia en t), $y_t$ (1 si comienza a estudiar en t), $z_t$ (1 si termina en t), y eventualmente una variable indicadora $w_t$ para la sesión de duración K.
   - Función Objetivo: Minimizar suma de costos variables $c_t \cdot x_t$ más costos de inicio $h_t \cdot y_t$.
   - Restricciones:
     - Restricciones de bloques prohibidos: $x_t = 0 \quad \forall t \in B$.
     - Lógica de inicio y fin: Vinculación estricta de $y_t$ y $z_t$ con $x_t$ y $x_{t-1}$. (Aplica cuidado especial para $t=1$ y $t=T$).
     - Tiempo mínimo de sesión ($U$): Si $y_t = 1$, debe implicar que $\sum_{k=0}^{U-1} x_{t+k} \ge U \cdot y_t$ (manejar los casos de borde para $t > T-U+1$).
     - Tiempo de descanso ($D$): Si $z_t = 1$, los siguientes $D$ periodos deben ser 0.
     - Mínimo H bloques: $\sum x_t \ge H$.
     - Restricción de sesión especial K: Uso correcto de variable auxiliar $w_t$ vinculada a $y_t$ para garantizar que al menos un inicio mantenga sesión por K bloques. $\sum w_t \ge 1$.
   - Naturaleza de las variables (todas binarias en $\{0,1\}$).

Entrega el código de manera que pueda ser copiado, pegado y compilado en Overleaf o VSCode sin arrojar ningún error de sintaxis en LaTeX. El código debe incluir ambientes `align*` o `equation` para todo el modelamiento matemático. Todo el texto descriptivo debe estar en idioma español con redacción académica de ingeniería. Produce SOLO el código de LaTeX delimitado por `latex ... `.
