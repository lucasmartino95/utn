# PEP8

**P**ython **E**nhancement **P**roposal es un documento que detalla recomendaciones para que nuestro código sea más legible. Abarca desde cómo nombrar variables, al número máximo de caracteres que una línea debe tener.

Es importante tener un **código resumido**, es decir, que no tenga cosas repetitivas.

Además, evitar usar condicionales anidados si no es necesario, ya que pueden dificultar la lectura del código.

## Reglas

### Indentado

En Python, se usa un **bloque indentado** para indicar que un determinado bloque de código pertenece a un contexto en particular. Por ejemplo:

```python
if condicion:
    # Código
```

### Tamaño máximo de línea

Limitar el **tamaño máximo de la línea a 79 caracteres** para evitar tener que hacer scroll horizontal y que el código sea más legible. Por ejemplo:

```python
numero_uno = 5
numero_dos = 3
numero_tres= 8

resultado = (numero_uno
          + numero_dos 
          - (numero_uno + numero_dos)
          - numero_tres)

print(resultado)
```

### Espacios en blanco

El uso de espacios en blanco mejora la legibilidad del código, por eso **PEP8** indica dónde debemos usar espacios y dónde no.

```python
# Correcto
x = 5

# Incorrecto
x=5
```

```python
# Correcto
if x == 5:
    pass

# Incorrecto
if x==5:
    pass
```

```python
# Correcto
var_a = 0
variable_b = 10
otra_variable_c = 3

# Incorrecto
var_a           = 0
variable_b      = 10
otra_variable_c = 3
```

### Variables

- Debe iniciar con un guión bajo o una letra.
- Que sea un sustantivo, que no sea un verbo.
- Letras en minúsculas y con guiones bajos para separar palabras.
- Los nombres de las variables son case-sensitive.

### Constantes

- Se define en mayúsculas.

# Paradigmas de programación

Un paradigma de programación es un enfoque, una manera de resolver un problema. Estos paradigmas pueden ser:

#### Programación estructurada

Programación secuencial. Usa ciclos y condiciones

```python
suma = 5 + 2
print(suma)
```

#### Programación funcional

Divide el programa en tareas pequeñas que son ejecutadas por funciones.

```python
def suma(num1, num2):
    print(num1 + num2)

suma(5, 2)
```

#### Programación orientada a objetos

Agrupa las funciones en entidades llamadas objetos, los cuales tienen características y comportamientos específicos.

```python
class Calculadora:

    def __init__(self, valor_inic):
        self.valor_inicial = valor_inic

    def suma(self, num1, num2):
        print(num1 + num2)

calc_1 = Calculadora(0)
calc_1.suma(5, 2)
```

#### Programación reactiva

Está orientada a flujos de datos y a la propagación de cambios. Los programas están diseñados para reaccionar automaticamente a eventos o cambios en los datos de forma asíncrona.

# Lenguaje compilado, lenguaje interpretado y lenguaje intermedio

Un **lenguaje compilado** requiere traducir el código fuente a código máquina. Una vez traducido (compilado), ya se puede ejecutar el programa a través del archivo que generó la traducción.

En cambio, un **lenguaje interpretado**, cada vez que se ejecuta un programa, realiza la traducción a código máquina en ese tiempo, lo que se denomina como traducción en tiempo de ejecución.

Por último, un **lenguaje intermedio o bytecode** compila el código fuente para generar un código intermedio que se ejecuta en una máquina virtual, la cual se encarga de interpretarlo o compilarlo ([JIT](https://es.wikipedia.org/wiki/Compilaci%C3%B3n_en_tiempo_de_ejecuci%C3%B3n)) en código máquina para el procesador.

**Por ejemplo** una **página web**, utiliza lenguajes de programación interpretados, ya que si los archivos que se ejecutan en tiempo de ejecución tienen algún error, la página web se muestra igual en función a si los errores son importantes o no. 

Si los errores son importantes, probablemente no se mostrará bien o no funcionará completamente la página web.