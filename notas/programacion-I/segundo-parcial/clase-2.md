# Copiar listas

## Superficial (shallow copy)

La shallow copy crea una nueva lista que contiene **referencias** a los mismos elementos que la lista original. Por lo tanto, si hacemos cambios en una de las listas, también se cambiará la otra.

```Python
import copy

lista_original = [[1,2], [3,4], [5,6]]

lista_copia = copy.copy(lista_original)

lista_copia[0][0] = 99

print("Lista Original", lista_original)
print("Lista Copia", lista_copia)
```

## Profunda (deep copy)

En cambio, la deep copy crea una nueva **lista independiente**, duplicando todos los objetos, incluso los anidados. Es decir que si hacemos cambios en la copia, no afectará a la lista original.

```Python
import copy

lista_original = [[1,2], [3,4], [5,6]]

lista_copia_profunda = copy.deepcopy(lista_original)

lista_copia_profunda[0][0] = 99

print("Lista Original", lista_original)
print("Lista Copia", lista_copia)
```

# Función enumerate y zip

### Enumerate

La función `enumarate` agrega un contador (índice) a los elementos de un iterable (una lista, por ejemplo).

```python
frutas = ["manzana", "plátano", "naranja"]

for indice, frutas in enumerate(frutas):
    print(f"Índice: {indice}, Fruta: {fruta}")
```

### Zip

Permite iterar múltiples listas a la vez

```python
nombres = ["Ana", "Luís", "Pedro"]
edades = [25, 30, 35]

for nombres, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")
```