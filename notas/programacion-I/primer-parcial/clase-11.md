# Matrices

Es una **estructura de datos bidimensional** que contiene elementos dispuestos en filas y columnas formando una tabla.

Para hacer matrices en **Python**, usaremos listas anidadas.

```python
alumno_1 = [4, 7, 8]
alumno_2 = [7, 9, 5]
alumno_3 = [4, 2, 7]

matriz_notas = [alumno_1, alumno_2, alumno_3]

print(matriz_notas)

alumno_1 = ["Perez", "José", 18]
alumno_2 = ["Suarez", "Nicolas", 20]
alumno_3 = ["Diaz", "Juan", 19]
alumno_4 = ["Ramirez", "Pedro", 30]
alumno_5 = ["Barceló", "Daniela", 24]

matriz_alumnos = [alumno_1, alumno_2, alumno_3, alumno_4, alumno_5]

print(matriz_alumnos)

lista_3 = [[1, 2, 3], [4, 5, 6]]


def mostrar_matriz(matriz: list) -> None:
    '''
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print("")
        

mostrar_matriz(matriz_alumnos)

# Para acceder a un elemento de la matriz podemos hacer:

print(matriz_alumnos[1][2]) # Imprimirá Juan
```

# Algoritmos de búsqueda

Podemos progamar de manera sencilla y que se tenga un rendimiento óptimo en memoria.

## ¿Cómo medir el rendimiento?

Medimos con un **cronómetro** cuánto tarda en ejecutarse nuestro algoritmo.

Otra opción es utilizar el **órden de complejidad** que toma en cuenta la complejidad de un algoritmo en el peor de los casos.

### Búsqueda lineal

Es la búsqueda más sencilla de programar

```python
lista = [3, 5, 6, 8, 9, 11]


def buscar_lineal(lista: list, buscado: int) -> int:
    for i in range(len(lista)):
        if lista[i] == buscado:
            return i
    
    print("No se encuentra el elemento buscado")


pos = buscar_lineal(lista, 8)

print(f"El 8 se encuentra en la posición {pos}")

pos = buscar_lineal(lista, 15)

print(f"El 15 se encuentra en la posición {pos}")
```