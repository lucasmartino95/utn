# Cadena de caracteres

Una cadena de caracteres es una **secuencia** de símbolos alfanuméricos, signos de puntuación, espacios, etc.

Por ejemplo:

```python
cadena = "Hello World"
```

Las cadenas de caracteres se pueden recorrer, por ejemplo:


```python
cadena = "Hello World"

for i in range(len(cadena)):
    if cadena[i] == "e":
        print(f"Posición {i}")
```

## Operaciones básicas

- **Acceso a caracteres individuales**: indexación [0]
- **Slicing (subcadenas)**: [1:0]
- **Longitud de la cadena**: función len
- **Concatenación**: operador +
- **Repetición de cadenas**: operador *
- **Comparación de cadenas**: operadores relacionales
- **Recorrido y búsqueda**: for

Notar que no podemos asignar nuevos valores a una cadena de caracteres ya que es un **objeto inmutable**.

### Comparación de cadenas

Para hacer comparaciones de cadenas, hay que recordar que son **case-sensitive**. Por lo que sería útil hacer una **normalización**, es decir, llevar ambas cadenas a comparar a un mismo formato.

La máquina lee los caracteres como números. Estos números son conocidos como **código ASCII**.

La función `ord()` permite obtener el código ASCII de un caracter. De esta manera podemos validar cadenas.

```python
# Notar que faltaría agregar una validación que compruebe que los dos caracteres sean letras

caracter_1 = "a"
caracter_2 = "A"
es_igual = False

diferencia = ord(caracter_1) - ord(caracter_2)

if (caracter_1 == caracter_2 
    or diferencia == 32
    or diferencia == -32):
    es_igual = True

print(es_igual)
```