# Funciones

Una función es un bloque de código que realiza una **tarea específica**.

A medida que los programas evolucionan, el código se puede volver **más complejo**. Esto se soluciona dividiendo el programa en **módulos más pequeños** que cumplan una tarea simple y bien acotada llamada funciones.

## Objetivos de una función

### Minificación

El programa se vuelve más simple de comprender ya que cada función se dedica a realizar una tarea específica.

### Depuración

La depuración queda acotada a cada función.

### Modificación

Las modificaciones al programa se reducen a cada módulo.

### Reutilización

Cada función se puede usar las veces que se quiera.

### Independencia

Cada función es independiente de otra.

## Componentes de una función

```python
# def: palabra reservada
# calcular_precio_con_iva: nombre
# valor_sin_iva: parámetro
# iva: parámetro opcional (deben ir siempre después de los parámetros formales)
# resultado: variable local
# resultado (return): valor del retorno
def calcular_precio_con_iva(valor_sin_iva, iva=21):
    '''
    Documentación
    '''
    resultado = valor_sin_iva * (1 + (iva / 100))
    return resultado
```

Otro ejemplo

```python
# Definición y desarrollo de la función
def buscar_maximo(cantidad_numeros: int = 5):
    for i in range(cantidad_numeros):
        numero_ingresado = int(input("Ingrese un número: "))
        if i == 0:
            maximo = numero_ingresado
        elif numero_ingresado > maximo:
            maximo = numero_ingresado
    return maximo


# Invocación o llamada de la función
maximo_1 = buscar_maximo()

print("Búsqueda dos")

# Invocación o llamada de la función
maximo_2 = buscar_maximo()

print(f"El máximo 1 es {maximo_1}")

print(f"El máximo 2 es {maximo_2}")
```

El nombre de la función debe contener un verbo, estar en minúsculas y si tiene muchas palabras, separado por guiones bajos.

### Parámetros formales y parámetros actuales

El **parámetro formal** es la variable que se utiliza dentro de una función, es decir la variable local

```python
def mostrar_mensaje(mensaje: str):
    print(mensaje)

texto = input("Ingrese texto a mostrar: ")

print(texto)

mostrar_mensaje("Perro")

# mensaje solo existe dentro del contexto de la función
print(mensaje)
```

El **parámetro actual** es la variable o dato que recibe la función al momento de ser invocada.

#### Scope

El término **scope** hace referencia al alcance de una variable, por ejemplo la palabra reservada **global** indica que estamos trabajando con una variable a nivel global dentro de por ejemplo una función.

En cambio, si no usamos la palabra global, todas las variables dentro de una función son **locales**.

```python
mi_nombre = "Lucas"

def imprimir_nombre():
    global mi_nombre
    mi_nombre = "Roberto"
    print(mi_nombre)

imprimir_nombre()
```

### Posición de los parámetros

```python
def restar(minuendo: int,
           sustraendo: int):
    '''
    '''
    return minuendo - sustraendo

# Los más común es utilizar los parámetros por posición
print(restar(4, 3))

# Alterar la posición de los parametros utiizando parámetros por nombre
print(restar(sustraendo = 3,
             minuendo = 4))
```

### Recomendaciones

- Aclarar tipo de valor de los parámetros y de retorno.
- Escribir documentación sobre la función.
- Evitar utilizar variables globales dentro de una función **(Evitar acomplamiento)**.
- Lograr una **cohesión** de las distintas partes de nuestro programa. Es decir, que cada parte funcione bien individualmente y en conjunto.

El **acoplamiento** es la dependencia de una función sobre otra.

```python
def restar(minuendo: int,
           sustraendo: int) -> int:
    '''
    '''
    return minuendo - sustraendo

# Los más común es utilizar los parámetros
# por posición
print(restar(4, 3))

# Alterar la posición de los parametros
print(restar(sustraendo = 3,
             minuendo = 4))
```

```python
def restar(mensaje: str) -> None:
    print(mensaje)

texto = input("Ingrese texto a mostrar: ")

mostrar_mensaje(texto)
```

Ejemplo de código sin acomplamiento, con cohesión

```python
def multiplicar(num_1: int, num_2: int = 3) -> int:
    return num_1 * num_2

def division(num_1: int, num_2: int) -> int:
    return num_1 / num_2

```

# Referencia

Una referencia es la dirección en memoria a la cual está vinculada una variable.

## Pasaje por valor y por referencia

En **Python** a una función siempre se le pasa los parámetros por referencia.

- **Por valor**: la función creará una copia local de la variable y cualquier modificación sobre ella no tendrá ningún efecto sobre la original

- **Por referencia**: la función recibirá la dirección de memoria de la variable original y podrá realizar modificaciones directamente sobre ella.

# Documentación

El objetivo de la documenatción es útil para indicarnos qué hace un determinado bloque de código, como las funciones. Es una **buena práctica**.

```python
def sumar(numero_a: int, numero_b: int) -> int:
    '''Función que se encarga de sumar dos números enteros

    Args:
        numero_a (int): Primer número
        numero_b (int): Segundo número

    Returns:
        int: Devuelve la suma entre estos dos números 
    '''
    suma = numero_a + numero_b
    return suma

print(sumar(5, 3))
```