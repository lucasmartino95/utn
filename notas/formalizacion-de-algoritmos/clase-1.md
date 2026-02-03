# Introducción
En este documento se detallan **temas fundamentales** de programación, como: 

- **Algoritmo**
- **Lenguajes  de programación**
- **Tipos de datos**
- **Variables y constantes** 
- **Expresion e instrucción**
- **Interacción con el usuario**
- **Operadores**
- **Interpolación**
- **Trabajar con porcentajes** 

## Algoritmo

Es un **conjunto de pasos lógicos y estructurados** que nos permiten dar solución a un problema.

### Estructura de un algoritmo

- **Entrada**: Es la introducción de datos para ser transformados.
- **Proceso**: Es el conjunto de operaciones a realizar para dar solución a un problema.
- **Salida**: Son los resultados obtenidos a través del proceso.

### Descomposición de un algoritmo

1. **Definición del problema**: Establecer resultados y objetivos para saber si los datos que se tienen son suficientes para lograr los fines propuestos.
2. **Análisis**: Organizar los datos de manera tal que se puedan usar en los cálculos siguientes.
3. **Diseño**: Solucionar un problema, aplicando conocimientos y datos existentes.
4. **Verificación a prueba de escritorio**: Comprobar que el algoritmo sirve o requiere modificarse.

### Cómo representar un algoritmo

Se puede representar un algoritmo a través de diagramas o código.

- **Diagrama**: [De flujo (flowchart)](https://es.wikipedia.org/wiki/Diagrama_de_flujo) o [Nassi-Shneiderman](https://es.wikipedia.org/wiki/Diagrama_Nassi-Shneiderman).
- **Código**: [Pseudocódigo](https://es.wikipedia.org/wiki/Pseudoc%C3%B3digo) o lenguaje real.

## Lenguajes de programación

Un **lenguaje de programación** es un conjunto formal de reglas, símbolos y palabras clave que permite a los humanos dar instrucciones a una computadora para ejecutar tareas específicas. 

Hay **muchos lenguajes de programación** que podemos utilizar para desarrollar nuestros programas. **Python** es uno de los lenguajes más sencillos de aprender ya que su **léxico** y **sintáxis** se asemejan mucho al inglés.

Existen lenguajes de **alto nivel** y lenguajes de **bajo nivel**.

#### Lenguajes de alto nivel
Se parecen al lenguaje que utilizamos los seres humanos para comunicarnos.

#### Lenguajes de bajo nivel
Son los que se acercan más al lenguaje máquina, es decir, al lenguaje que es directamente entendible por el hardware de una computadora.

#### Algunos conceptos fundamentales

- **Programa**: Es un conjunto de instrucciones, escritas en un lenguaje de programación, que le indica a la computadora cómo realizar una tarea específica.
- **Alfabeto**: Un conjunto de símbolos utilizados para formar palabras de un determinado lenguaje.
- **Léxico**: (también conocido como diccionario) Un conjunto de palabras que el lenguaje ofrece a sus usuarios.
- **Sintáxis**: Un conjunto de reglas utilizadas para precisar si una determinada cadena de palabras forma una oración válida. Por ejemplo, "Soy una serpiente" es una frase sintácticamente correcta, mientras que "Yo serpiente soy una" no lo es.
- **Semántica**: Un conjunto de reglas que determinan si una frase tiene sentido. Por ejemplo, "Me comí una dona" tiene sentido, pero "Una dona me comió" no lo tiene.

Un programa escrito en un lenguaje de programación se denomina **código fuente**. Traducir este código fuente a lenguaje de máquina se puede hacer de dos maneras, las cuales también definen si un **lenguaje es compilado o interpretado**:

- **Compilado**: El código fuente se traduce una sola vez, al obtener el archivo que contiene el código máquina.
- **Interpretado**: Cualquier usuario del código fuente puede traducir el programa cada vez que se quiere ejecutar.

## Tipos de datos

En programación existen diferentes tipos de datos, los cuales indican **qué tipo de información** representa un valor.

#### Numéricos
- **Entero**: 7815158, 17, -2
- **Punto flotante**: 148562.4, 3.141592, -1.5

#### Alfanuméricos
- **Carácter simple**: "a", "@", "2"
- **Cadena de caracteres**: "Hola", "@", "Lo que sea"

#### Lógicos
- **Verdadero**: true
- **Falso**: false

Para saber el tipo de dato de un valor, podemos usar la función `type()`:

```python
print(type(5)) # Devolverá <class 'int'>
print(type("Hola")) # Devolverá <class 'str'>
print(type(True)) # Devolverá <class 'bool'>
```

## Variables y constantes

Una **variable** es un espacio en la memoria que **guarda un valor que puede cambiar** durante la ejecución de un programa.

Una **constante** es un valor que **no cambia** durante la ejecución de un programa.

### Variables en Python

 ```python
 # Crea una variable llamada var y guarda el valor 1
var = 1
print(var) # Imprime el valor de var

# Toma el valor de var, sumale 1 y vuelvelo a guardar en la variable var
var = var + 1
print(var) # Imprime el nuevo valor de var
 ```

### Constantes en Python

En **Python** no existen las constantes, sin embargo se puede seguir una convención para mantener el código legible. Se trata de escribir el **nombre de la constante en mayúsculas**.

```python
TITULO_CURSO = "curso introducción"
```

#### Nota sobre variables y constantes

Si **no necesitamos** utilizar el valor de una variable o constante más de una vez, es recomendable **no crear variables** ya que nos ahorramos ocupar espacio en la memoria, lo cual hace que nuestro programa tenga mejor rendimiento.

#### Nombrando variables
Existe una [convención de nomenclaturas](https://www.python.org/dev/peps/pep-0008/) para variables y funciones:

- Los nombres de las variables o funciones deben estar en minúsculas, con palabras separadas por guiones bajos. Por ejemplo: var, my_variable. Esto es conocido como **snake_case**.
- También es posible usar letras mixtas, por ejemplo: myVariable. Pero solo en contextos donde ese estilo es el predominante.
- Por último, el nombre de la variable o función no puede ser igual a alguna de las [palabras reservadas en Python](https://docs.python.org/3/reference/lexical_analysis.html#keywords) (o palabras clave).

## Expresión e instrucción

Una **expresión** es una combinación de elementos que se evalúa para producir un único valor. Por ejemplo:

```python
9 * 5
```

Una **instrucción** es una orden o comando que le indica a la computadora qué acción específica debe realizar. Por ejemplo:

```python
print(9 * 5) # Imprimir 45
```
## Interacción con el usuario

La función `input()` es capaz de **leer datos ingresados** por el usuario. Luego, podemos guardar esos datos en una variable para utilizarlos después. Por ejemplo:

```python
algo = input("Escribir lo que sea...")
print("Hmm..",algo,"...¿en serio?")
```

Hay que resaltar que la función `input()` **devuelve una cadena de caracteres**, por lo que no podemos hacer operaciones matemáticas, a menos que utilicemos funciones que Python ofrece para convertir datos. El proceso de convertir datos es conocido como **casteo** o **casting**. Por ejemplo:

```python
numero = int(input("Ingresa un número: "))
resultado = numero * 2
print(numero,"multiplicado por 2 es", resultado)
```

El siguiente ejemplo calcula la longitud de la hipotenusa. Debido a que `print()` acepta una expresión como argumento, podemos hacer el calculo de la hipotenusa pasandole como argumento la expresión.

```python
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es:",(leg_a**2 + leg_b** 2) ** .5)
```

## Operadores

### Aritméticos
Son los **símbolos** que representan las acciones fundamentales que se realizan con números:

```python
print(9 + 5) # Suma
print(9 - 5) # Resta
print(9 * 5) # Multiplicación
print(9 / 5) # División
print(9 // 5) # Devuelve el cociente entero de dos números
print(9 ** 5) # Potenciación
print(9 % 5) # Devuelve el resto del cociente entre números
```

Los **operadores aritméticos** siguen la [jerarquía de prioridades](https://edu.gcfglobal.org/es/algebra/orden-de-las-operaciones/1/), es decir, algunos operadores actúan antes que otros. Por ejemplo:

```python
2 + 3 * 5
```

Primero se realiza la multiplicación, y luego la suma, por lo que quedaría:

```python
2 + 15 # Resultado 17
```

#### Operador aritmético de raíz

Para hacer la raíz de un número podemos utilizar fracciones. Por ejemplo:


```python
raiz_cuadrada = 4 ** (1/2)
raiz_cubica = 27 ** (1/3)

print(raiz_cuadrada, raiz_cubica)
```

### De cadena y de replicación

El signo + (más), al ser aplicado a dos cadenas, se convierte en un **operador de concatenación**:

```python
fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias.")
print("\nTu nombre es " + fnam + " " + lnam + ".")
```

El signo * (asterisco) al ser aplicado a una cadena y a un número, se convierte en un **operador de replicación**:

```python
print("James" * 3) # Imprimirá JamesJamesJames
print(3 * "an") # Imprimirá ananan
print(5 * "2") # Imprimirá "22222"
```

### De incremento y decremento

En Python no existe el operador ++ ni --, para lograr el mismo resultado, se utilizan **operadores compuestos**:

```python
x = 5
x = x + 1 # O bien se puede utilizar: x += 1
print(x)
```

```python
x = 5
x = x - 1 # O bien se puede utilizar: x -= 1
print(x)
```
 
Lista de operadores compuestos:


| Operador | Forma abreviada | Forma común |
|---|---|---|
|+=|x += 2|x = x + 2|
|-=|x -= 2|x = x - 2|
|*=|x *= 2|x = x * 2|
|/=|x /= 2|x = x / 2|
|%=|x %=2|x = x % 2|
|//=|x //= 2|x = x // 2|
|**=|x **= 2|x = x ** 2|

### Relacionales o de comparación

Los operadores relacionales **toman números y devuelven como resultado un valor lógico**, es decir, verdadero o falso.

Lista de operadores relacionales:

| Operador | Nombre | Ejemplo | Resultado |
|---|---|---|---|
| < | Menor que | 4 < 5 | Verdadero |
| <= | Menor o igual que | 5 <= 5| Verdadero |
| > | Mayor que | 4 > 5 | Falso |
| >= | Mayor o igual que | 5 >= 5 | Verdadero |
| == | Igual que | 4 == 5 | Falso |
| != | Distinto de | 4 != 5 | Verdadero |

## Interpolación

La **interpolación** se refiere a la inserción de valores de variables o expresiones en una cadena de texto. En **Python** se puede utilizar **f-strings**. Por ejemplo:

```python
name = "Lucas"
print(f"Hola {name}")
```

Otro ejemplo:

```python
numero_uno = 5
numero_dos = 3
print(f"La suma de {numero_uno} y {numero_dos} es: {numero_uno + numero_dos}")
```

## Trabajar con porcentajes

Los **porcentajes** son una forma de **expresar un número como una fracción de 100**. Por ejemplo, el 50% es igual a 50/100 o 0.5.

```python
# Convertir un número a porcentaje
numero = 0.75
porcentaje = numero * 100
print(porcentaje)

# Encontrar el porcentaje de un número utilizando regla de tres simple
numero = 200
porcentaje = 15
resultado = (numero * porcentaje) / 100 # El 15% de 200 es 30
print(resultado) # 30

# Incrementar un número por un porcentaje
numero = 100
porcentaje = 20
incremento = (numero * porcentaje) / 100 # El 20% de 100 es 20
nuevo_numero = numero + incremento # 100 + 20 = 120
print(nuevo_numero) # 120
```