# Métodos

Son **funciones** que se aplican sobre un determinado tipo de dato, por ejemplo las listas. Los métodos pertenecen a clases.

Algunos métodos más usados son:

`append` `insert` `extend` `remove` `pop` `clear` `index` `sort` `reverse`

## Eliminar elementos de una lista

```python
lista = [1, 2, 3, 4]
del lista[0]

print(lista)
```

```python
lista = [1, 2, 3, 4]
del lista[1:3]

print(lista)
```

## Copiado de listas

Podemos hacer distintos tipos de copia de listas

- **Shallow copy**
- **Deep copy**

# Tipos de datos avanzados

- **Tuplas**: Son similares a listas, con la diferencia que son inmutables. También podemos desempaquetar sus elementos.

```python
tupla = (3, 2, 5)

num1, num2, num3 = tupla

print(num1)
print(num2)
print(num3)
```

- **Sets**: Los elementos de un set son únicos, no contiene elementos duplicados. Los sets no respetan el orden que tenían al ser declarados. Son mutables.

```python
ejemplo_set = {4, 3, 1, 4, 2, 5, 6, 3, 1}

print(ejemplo_set)
```

```python
ejemplo_set = {4, 3, 1, 4, 2, 5, 6, 3, 1}
ejemplo_2_set = {7, 8, 9, 1}

ejemplo_set.union(ejemplo_2_set)

print(ejemplo_set)
```

- **Diccionarios**: Es una colección de elementos compuesto por una clave (key), que es única y un valor (value), contenidos entre llaves. La ventaja es que podemos acceder a un valor a través de una llave y no de una posición.

```python
ejemplo_diccionario = {
    "nombre":"Juan",
    "edad": 21,
    "apellido": "Perez"
}

print(ejemplo_diccionario["edad"])


for key in ejemplo_diccionario.keys():
    print(key)


for clave, valor in ejemplo_diccionario.items():
    print(f"clave = {clave}")
    print(f"valor = {valor}")
    print()
```