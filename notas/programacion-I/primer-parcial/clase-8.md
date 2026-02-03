# Recursividad

Repite una función sobre sí misima una **n** cantidad de veces hasta llegar a un punto de salida.

```python
# Cuenta regresiva con for
numero = int(input("Ingrese un número para iniciar cuenta regresiva: "))

for i in range(numero, -1, -1):
    print(i)

# Cuenta regresiva con función recursiva
def contar_regresivamente(n: int) -> None:
    '''
    Cuenta regresivamente

    Recibe un número desde el que inicia la cuenta

    No retorna nada
    '''

    if n == -1:
        print("Finalizó")
    else:
        print(n)
        contar_regresivamente(n - 1)

print("Ahora se aplica la recursividad")

contar_regresivamente(10)
```

Otro ejemplo de recursividad

```python
# Factorial de 5
# 5!
# 5 * 4 * 3 * 2 * 1

factorial = int(input("Ingrese el número del que quiere calcular el factorial: "))

def calcular_factorial(n: int) -> int:

    if n == 0: # Caso base
        resultado = 1
    else:
        resultado = n * calcular_factorial(n - 1)

    return resultado


resultado_ejemplo = calcular_factorial(factorial)

print(f"El factorial de {factorial} es {resultado_ejemplo}")
```

# Espacio en memoria

Cada vez que la función se llama a sí misma, **Python** guarda en memoria con diferente dirección a la función llamada. La **pila de llamadas** de una función recursiva tiene un límite, caso contrario nos arrojara un error: **RecursionError**.

```python
def imprimir_numero(n: int) -> None:
    if n > int(-1000):
        imprimir_numero(n - 1)

    print(n)

imprimir_numero(0)
```

## Ventajas de usar recursividad

- Es una solución elegante.
- Simplicidad conceptual
- Facilidad de mantenimiento

## Desventajas de usar recursivdad

- Consumo de memoria
- Eficiencia
- Límite de recursión
- Posibles cálculos redundantes
