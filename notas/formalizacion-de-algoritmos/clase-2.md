# Estructuras condicionales

Una **instrucción condicional** permite hacer algo si se cumple una condición, y no hacerlo si no se cumple.

También podemos decir, que **bifurcan** el código, es decir, **alteran el flujo secuencial** para que el programa tome decisiones. Esto se llama, **flujo de selección**.

Un **flujo de selección** consta de las siguientes alternativas:

- Flujo de selección simple: (if).
- Flujo de selección doble (if-else).
- Flujo de selección anidado.

A continuación se puede ver una instrucción condicional escrita de **manera informal** (Pseudocódigo).

```
si (verdad o falso): realiza alguna acción si es verdad
```

En **Python** la palabra clave asociada a esta instrucción es `if`. Por ejemplo:

```python
if 25 >= 8:
    print("Puedo salir a caminar")
```

Si la condición es falsa y queremos hacer algo cuando esto sucede, podemos usar la palabra clave `else`. Por ejemplo:

```python
if 7 >= 8:
    print("Puedo salir a caminar")
else:
    print("No puedo salir a caminar")
```

También podemos establecer la condición de entrada. En el siguiente caso, utilizando `True` en la primer condición, siempre se ejecutará el código dentro de esa condición.


```python
if True:
    print("Puedo salir a caminar")
else:
    print("No puedo salir a caminar")
```

### Instrucciones if-else anidadas

Podemos **anidar** nuestras instrucciones condicionales si necesitamos hacer nuestro código **un poco más complejo**, donde se evalúan múltiples condiciones en un orden específico.

```python
edad = 25
if edad >= 18:
    if edad > 22:
        print("Es mayor de edad y mayor a 22.")
    else:
        print("Es mayor de edad pero menor a 22.")
else:
    print("Es menor de edad.")
```

La **sangria** mejora la legibilidad y hace que el código sea más fácil de entender y rastrear. Se debe elegir entre el **espacio o tabulador** para lograr la sangria. Además, es una **regla de sintáxis** en Python, para ejecutar bloques de código.

### Instrucción elif

Por último, si queremos verificar más de una condición y detener el programa cuando se encuentre la primer condición verdadera, podemos usar `elif`. Por ejemplo:

```python
valor = int(input("Ingrese un numero del 1 al 3: "))

if valor == 1:
    print("Es lunes.")
elif valor == 2:
    print("Es Martes.")
elif valor == 3:
    print("Es Miercoles.")
else:
    print("No ha elegido ningun valor entre 1 y 3")
```

### Alternativa de la instrucción elif

En 2021, **Python** añadió una característica para hacer **estructuras condicionales múltiples**: match-case.

```python
print("MENÚ DE OPCIONES")
print("[1] Ventas")
print("[2] Soporte")
print("[3] Administración")

opcion = int(input("Elegir opción: "))

match opcion:
    case 1:
        print("VENTAS")
    case 2:
        print("SOPORTE")
    case 3:
        print("ADMINISTRACIÓN")
    case _: # Comodín: En caso de que no se cumplan las sentencias anteriores
        print("Opción inexsistente")
```

### Comentarios

Los comentarios son útiles para **aclarar** lo que hace determinado bloque de código. Además, los comentarios son ignorados por el intérprete de Python, solo están en el código como referencia.

# Operadores lógicos

Los **operadores lógicos** sirven para combinar expresiones booleanas (que devuelven verdadero o falso) y así construir condiciones más complejas.

En **Python**, podemos encontrar los siguientes operadores lógicos:

- **Conjunción (Y / AND)** : "Para considerar aprobado al alumno, debe aprobar ambos exámenes: oral y escrito". Depende del cumplimiento simultaneo de dos condiciones.
- **Disyunción (O / OR)**: "Para considerar aprobado al alumno, debe aprobar algún examen: oral o escrito".  Para aprobar el examen depende de al menos una de las dos condiciones.
- **Negación (NO / NOT)**: Conectivo monádico (una sola proposición).

#### Operador AND

Es un **operador binario** con una prioridad inferior a la expresada por los operadores de comparación.

```python
vida = 3
energia = 70

print(vida > 0 and energia > 50)
```

Podemos determinar el resultado de la expresión utilizando la **tabla de la verdad**:

|#|Argumento A|Argumento B|A and B|
|---|---|---|---|
|1|False|False|False|
|2|False|True|False|
|3|True|False|False|
|4|True|True|True|

#### Operador OR

Es un **operador binario** con una prioridad más baja que `and`

```python
vida = 0
energia = 70

print(vida > 0 or energia > 50)
```

Tabla de la verdad:

|#|Argumento A|Argumento B|A or B|
|---|---|---|---|
|1|False|False|False|
|2|False|True|True|
|3|True|False|True|
|4|True|True|True|

#### Operador NOT

Es un **operador unario** que realiza una negación lógica. Su funcionamiento es simple: **convierte la verdad en falso y lo falso en verdad**. Su prioridad es muy alta: igual que el unario + y -

```python
soy_robot = True
print(soy_robot)

soy_robot = not soy_robot
print(soy_robot)

valorA = False
print(not valorA)
```

# Contadores y acumuladores

Un **contador** es una variable entera que se utiliza para llevar la cuenta del número de veces que ocurre un evento o se cumple una condición. 

Por ejemplo, al visitar el departamento de servicio al cliente en una empresa, los clientes para obtener un turno deben tomar un ticket. Un letrero electrónico indica el número del cliente que se está atendiendo, luego éste número cambia incrementándose en 1 para anunciar el siguiente turno a ser atendido.

Tiene dos características:

- Siempre tiene un valor inicial.
- El valor nuevo del contador es el resultado del valor anterior más una constante.

```python
contador = 0
contador = contador + 1
print(contador)
```

Un **contador** puede tener cambios de forma ascendente o decreciente.

```python
contador = 4
contador = contador - 1
print(contador)
contador = contador - 1
print(contador)
contador = contador - 1
print(contador)
contador = contador - 1
print(contador)
```

Un **acumulador** tiene las mismas características que el contador, solo que el valor de incremento o decremento es un valor variable.

Por ejemplo, una cuenta de ahorros puede representarse en un algoritmo mediante un acumulador, pues quien ahorra no siempre lo hará con una cantidad fija en la cuenta: un día deposita 10, otro día deposita 30, otro deposita 5.

Con el ejemplo de ahorro, se puede determinar que en el acumulador no siempre se añade un valor positivo, pues cuando se hace un retiro, se puede interpretar como que el valor añadido es negativo.

```python
acumulador = 0
acumulador = acumulador + 20
acumulador = acumulador + 40
print(acumulador)
```

# Redundancia

La redundancia es **algo que se repite innecesariamente**. En este caso, hablamos de redundancia cuando hacemos preguntas repetitivas. Por ejemplo:

```python
edad = 17
if edad >= 18:
    print("Es mayor de edad.")
elif numero < 18:
    print("No es mayor de edad.")
```

No es necesario utilizar `elif` para hacer otra pregunta, ya que si la edad no es mayor o igual que 18, la edad sí o sí tiene que ser menor que 18.

```python
edad = 17
if edad >= 18:
    print("Es mayor de edad.")
else:
    print("No es mayor de edad.")
```
