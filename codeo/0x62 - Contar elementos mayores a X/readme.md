0x62 - Contar elementos mayores a X
Dado un arreglo de enteros, queremos responder esta pregunta: ¿Cuántos elementos hay mayores a X?

Escribe un programa que recibe varias "consultas", cada una con un valor diferente de X y para cada consulta imprime el número de elementos en el arreglo que son mayores a X.

Entrada
La entrada contiene varias líneas:

La primera línea contiene N, el número de elementos en el arreglo.
La segunda línea contiene N enteros Ai para 0 ≤ i < N, los elementos del arreglo. Estos números están separados por espacios. Está garantizado que Ai satisface -109 ≤ Ai ≤ 109.
La tercera línea contiene C, el número de consultas.
Luego vienen C líneas, cada una con un consulta descrita por un entero X. Está garantizado que -109 ≤ X ≤ 109.
Salida
La salida debe tener exactamente C líneas (una por consulta).

Para cada consulta, escribe el número de elementos en el arreglo que son mayores a X.

Entrada de ejemplo
5
3 4 1 2 2
3
0
1
4
Salida de ejemplo
5
4
0
Explicación de la entrada y salida de ejemplo
La entrada nos da un arreglo A = [3, 4, 1, 2, 2] con 5 elementos. Luego nos da 3 consultas:

La primera consulta es X = 0. Todos los elementos de A son mayores a 0, entonces la respuesta es 5.
La segunda consulta es X = 1. Hay 4 elementos mayores a 1, específicamente 3, 4, 2 y 2, entonces la respuesta es 4.
La tercera y última consulta es X = 4. No hay ningún elemento en A que sea mayor a 4, entonces la respuesta es 0.
Restricciones
Está garantizado que 1 ≤ N ≤ 100 y 1 ≤ C ≤ 100.
