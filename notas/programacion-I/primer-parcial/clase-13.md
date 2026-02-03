# Ordenamiento

Los algoritmos de ordenamiento son un conjunto de instrucciones que buscan organizar elementos en un orden particular.

## Clasificación

Se clasifican según:

- Cantidad de intercambios
- Número de comparaciones
- Cantidad de espacio adicional
- Si usa recursividad o no

### Ordenamiento por burbujeo (bubble sort)

```python
lista = [9, 3, 2, 7, 5, 4, 1]

def ordenar_x_burbujeo(lista: list) -> list:
    '''
    Recorre una lista n -1 veces y ordena elementos adyacentes

    Recibe una lista

    Retorna una lista
    '''

    if type(lista) != list:
        print("El parámetro que recibe debe ser una lista")
        return # Es lo mismo que poner return None

    n = len(lista)

    for i in range(n):
        print(f"Iteración {i}")
        intercambio = False
        for j in range(0, n - 1 - i):
            if lista[j] > lista[j + 1]:
                intercambio = True
                mayor = lista[j + 1]
                lista[j + 1] = lista[j]
                lista[j] = mayor

                print(f"{mayor} se cambió por {lista[j + 1]}")
            
        if intercambio == False:
            break
    return lista
```

### Ordenamiento por selección

```python
lista = [9, 3, 2, 7, 5, 4, 1]

def ordenar_x_seleccion(lista: list) -> list:
    '''
    Ubica iterativamente el menor valor en el índice más bajo

    Recibe un listado

    Retorna un listado
    '''

    if type(lista) != list:
        print("El parámetro de la función debe ser una lista")
        return

    for i in range(len(lista) - 1):

        indice_menor = i

        print(f"iteración {i}")

        for j in range(i + 1, len(lista)):
            if lista[j] < lista[indice_menor]:
                indice_menor = j
            
        if indice_menor != i:
            menor = lista[indice_menor]
            lista[indice_menor] = lista[i]
            lista[i] = menor

    return lista
```

### Ordenamiento quicksort

```python
```

### Ordenamiento por inserción

```python

lista = [9, 3, 2, 7, 5, 4, 1]

def ordenar_x_insercion(lista: list) -> list:
    for i in range(len(lista)):
        print(f"i = {i}")

        elemento_auxiliar = lista[i]

        j = i - 1

        while j >= 0 and elemento_auxiliar < lista[j]:
            lista[j + 1] = lista[j]

            j -= 1
        
        lista[j + 1] = elemento_auxiliar

    return lista

print(ordenar_x_insercion(lista))
```