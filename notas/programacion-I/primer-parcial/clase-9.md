# Vector

Es un **arreglo unidimensional**. Cada elemento dentro de la **lista o vector** tiene una posición única. Por lo que podremos acceder al elemento indicando su posición. Permite **organizar y ordenar** cantidades de datos grandes. También permite la **escalabilidad** del código. La lista es un **objeto mutable**

```python
notas_perez = [5, 4, 7, 2, 8, 9, 9, 4, 6, 7, 8,2]

for i in range(len(notas_perez)):
    if notas_perez[i] < 6:
        print(f"Perez aún no aprobó la materia {i}")
```

Otros ejemplos de cómo crear una lista

```python
lista_1 = list((1, 2, 3, 66, 7))
print(lista_1)
```

```python
lista = [0] * 5
print(lista)
```

```python
def inicializar_lista(cantidad_elementos: int, valor_por_defecto: any = 0) -> list:
    return [valor_por_defecto] * cantidad_elementos


lista = inicializar_lista(9, "m")
print(lista)
```

### Acceder a un elemento de la lista

```python
lista = [1, 2, 3]

print(lista[0]) # Imprimirá 1
print(lista[-1]) # Imprimirá 3
```

### Mostrar una lista y modificar elementos

```python
def inicializar_lista(cantidad_elementos: int, valor_por_defecto: any = 0) -> list:
    return [valor_por_defecto] * cantidad_elementos


def mostrar_lista(lista: list):
    for i in range(len(lista)):
        print(f"Indice {i} = {lista[i]}", end = "-")
        

lista_2 = inicializar_lista(9, "m")    

lista_2[2] = "a" # Modifica el elemento de la posición 2

mostrar_lista(lista_2)
```

### Carga de listas

#### Secuencial

```python
def inicializar_lista(cantidad_elementos: int, valor_por_defecto: any = 0) -> list:
    return [valor_por_defecto] * cantidad_elementos


def mostrar_lista(lista: list):
    for i in range(len(lista)):
        print(f"Indice {i} = {lista[i]}", end="-")
        

def cargar_lista(lista: list, mensaje: str) -> list:
    for i in range(len(lista)):
        print(f"Posición {i}")
        lista[i] = input(mensaje)

    # return lista


lista_2 = inicializar_lista(9, "m")    

cargar_lista(lista_2, "Ingrese cantidad de camisetas: ")

mostrar_lista(lista_2)
```

#### Aleatoria o distribuido

```python
def cargar_distribuido(lista: list, posicion: int) -> list:
    lista_2[posicion] = input(f"Ingrese nuevo valor para posición {posicion}")
```

#### Nota

Es mejor trabajar con **posiciones** para estandarizar los algoritmos donde utilicemos listas. Es decir, que funcione de la misma manera con diferentes listas.

## Memoria stack y memoria heap

La **memoria stack** es estática, tiene un tamaño fijo y predefinado. Almacena variables locales y retornos de una función. Es **gestionada de manera automática** en tiempo de ejecución.

Por otro lado, la **memoria heap** es dinámica, tiende a crecer mucho. Almacena objetos, listas y diccionarios. Es gestionada de manera manual o automática.

- **Manual**: Lo hace el programador. Es el encargado de reservar y liberar la memoria para una variable determinada, por ejemplo en en el lenguaje C.

- **Automática**: Lo gestiona el lenguaje. El mismo reserva espacio en memoria dinámica y al momento de liberar la misma se apoya en un software llamado: Recolector de Basura.