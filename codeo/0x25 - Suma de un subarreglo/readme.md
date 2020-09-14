0x25 - Suma de un subarreglo
Supongamos que tenemos un arreglo llamado A.

Un subarreglo de A está definido como cualquier bloque de elementos consecutivos en A. Por ejemplo, si A = [5, -2, 1, 4], A tiene 10 subarreglos que son:

[5]
[5, -2]
[5, -2, 1]
[5, -2, 1, 4]
[-2]
[-2, 1]
[-2, 1, 4]
[1]
[1, 4]
[4].
Por otro lado, [5, -2, 4] no es un subarreglo de A porque estos elementos no aparecen de forma consecutiva en A.

Una manera de describir un subarreglo es usando dos índices de A que describen dónde empieza y dónde termina el subarreglo. Llamemos p al índice izquierdo y q al índice derecho. Por ejemplo:

El subarreglo [5, -2] se describe con p = 0 y q = 1;
El subarreglo [-2, 1, 4] se describe con p = 1 y q = 3;
El subarreglo [1] se describe con p = 2 y q = 2;
El subarreglo [5, -2, 1, 4] se describe con p = 0 y q = 3.
Escribe un programa que recibe varias "consultas" de la forma p, q y para cada consulta calcula la suma de todos los elementos del subarreglo que empieza en p y termina en q.

Entrada
La entrada contiene varias líneas:

La primera línea contiene N, el número de elementos en el arreglo.
La segunda línea contiene N enteros Ai para 0 ≤ i < N, los elementos del arreglo. Estos números están separados por espacios. Está garantizado que Ai satisface -104 ≤ Ai ≤ 104.
La tercera línea contiene C, el número de consultas.
Luego vienen C líneas, cada una con un consulta descrita por dos índices p y q separados por un espacio. Está garantizado que 0 ≤ p ≤ q < N (es decir, p y q son índices válidos).
Salida
La salida debe tener exactamente C líneas (una por consulta).

Para cada consulta, escribe una línea con la suma de los elementos del subarreglo que empieza en p y termina en q.

Entrada de ejemplo
4
5 -2 1 4
4
0 1
1 3
2 2
0 3
Salida de ejemplo
3
3
1
8
Explicación de la entrada y salida de ejemplo
La entrada nos da un arreglo A = [5, -2, 1, 4] y 4 consultas:

La primera consulta (0 1) corresponde al subarreglo [5 -2]. La suma de estos elementos es 3.
La segunda consulta (1 3) corresponde al subarreglo [-2 1 4]. La suma de estos elementos también es 3 (por casualidad).
La tercera consulta (2 2) corresponde al subarreglo [1]. La suma de este único elemento es 1.
La cuarta y última consulta (0 3) corresponde al arreglo completo, [5 -2 1 4]. La suma de estos elementos es 8.
Restricciones
En 50% de los casos, 1 ≤ N ≤ 100 y 1 ≤ C ≤ 100.
En el otro 50% de los casos, 1 ≤ N ≤ 50,000 y 1 ≤ C ≤ 50,000.

