# For

A diferencia del while, el **for** define de antemano el número de iteraciones que se va a utilizar.

Se suele utilizar el **for** con la función **range**. 

```python
# Cuando se le pasa un solo parametro, el rango inicia en 0.
rango = range(10)

print(rango)
print(type(rango))

for numero in rango:
    print(numero)
```

```python
# El rango va desde el 1 hasta el 2
rango = range(1, 3)

print(rango)
print(type(rango))

for numero in rango:
    print(numero)
```

```python
# El rango comienza en 10 y decrementa de a 3 hasta llegar al limite (1)
rango = range(10, 1, -3)

print(rango)
print(type(rango))

for numero in rango:
    print(numero)
```

```python
rango = range(2, 11, 2)

for numero in rango:
    cuadrado = numero ** 2
    print(f"El cuadrado de {numero} es {cuadrado}")
```

Ejemplo usando listas

```python
lista = [1, 2, 3, 4, 5]

list(range(1, 6))

for i in range(len(lista)):
    print(lista[i])
```

```python
notas_alumno = [2, 7, 8, 9, 10, 5, 3, 1]
suma = 0

for i in range(len(notas_alumno)):

    print(f"El indice es {i}")
    print(f"La nota es: {notas_alumno[i]}")

    suma += notas_alumno[i]

promedio = suma / len(notas_alumno)
print(f"El promedio es {promedio}")
```

## For each

El **foreach** accede directamente a los elementos de un vector o lista. En **Python** no existe la palabra **foreach**

En **Python** el foreach se utiliza de esta manera

```python
rango = range(10)

#foreach
for numero in rango:
    print(numero)
```

### Break

El **break** es una palabra reservada que se utiliza para detener la ejecución de una estructura repetitiva

```python
limite_memoria = 100

notas_alumno = list(range(140))

for i in range(len(notas_alumno)):
    print(i)

    if i == limite_memoria:
        break
```

### Continue

El **continue** es una palabra reservada que se utiliza para saltear una iteración en una estructura repetitiva

```python
for numero in range(14, 31):
    if numero % 5 == 0:
        continue
    print(numero)
```

## For anidado

```python
# Bucle de dos dimensiones

for i in range(1, 4):
    print(f"i es: {i}")
    for j in range(3):
        print(f"{i} {j}")
```

```python
# Bucle de tres dimensiones

for i in range(1, 4):
    print(f"i es: {i}")
    for j in range(3):
        print(f"{i} {j}")
        for k in range(5):
            print(f"k es {k}")
```
