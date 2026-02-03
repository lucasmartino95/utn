## A - Fundamentos de programación

1. ¿Qué es un paradigma de programación?¿Es correcto decir que python es un lenguaje multiparadigma?

Un **paradigma** en programación es una forma de resolver problemas. Es correcto decir que **Python es multiparadigma** ya que puede ser un lenguaje funcional u orientado a objetos.

2. ¿Qué diferencia hay entre un lenguaje compilado y uno interpretado?

Un **lenguaje compilado** primero traduce todo el código fuente a código máquina para que luego sea ejecutado. En cambio, un **lenguaje interpretado** hace la traducción cuando se va a ejecutar el programa, línea por línea.

3. ¿Qué es una variable en python?

Una variable en **Python** es una etiqueta que apunta a un valor.

4. ¿Qué tipos de datos existen?

Existen los siguientes **tipos de datos**: numéricos (int, float), alfanuméricos (str) y lógicos (True, False), compuestos (listas, diccionarios)

5. ¿Cuál es la utilidad de las estructuras de control?

Permiten **controlar el flujo** de nuestro programa para que pueda tomar diferentes caminos en lugar de ser secuencial.

6. ¿Qué es PEP y qué propone?

**PEP** es una guía de estilo de **Python**. Propone establecer reglas de estilo para escribir nuestro código haciendo que sea más legible y familiar a otros programadores.

7. ¿Cuál es la utilidad de los bucles for?¿Qué es continue y qué es break?

Los bucles **for** sirven para repetir instrucciones una determinada cantidad de veces. La palabra reservada **continue** es para saltear una iteración en caso de que se cumpla una condición. La palabra reservada **break** sirve para salir del bucle en caso de que se cumpla una condición.

## B - Funciones

8. ¿Qué es una función, para qué sirve y cuáles son sus objetivos?

Una **función** es un bloque de código que contiene instrucciones. Sirve para reutilizar las instrucciones que contiene y sus objetivos pueden ser: no repetir código, modularizar programa, hacer más legible nuestro programa.

9. ¿Cuáles son los componentes de una función?

Una **función** tiene nombre, puede tener parámetros y cuerpo.

10. ¿Qué hacen las palabras reservadas def y return?

La palabra **def** se usa para definir una función y **return** para que la función devuelva un valor cuando es invocada.

11. ¿Qué es un parámetro formal y cómo se utiliza?

Un **parámetro formal** es una variable local que se utiliza dentro de una función. Se coloca entre los () de la función y dentro del cuerpo de la función es utilizada como una variable.

12. ¿Qué es un parámetro opcional?

Un **parámetro opcional** es una variable local de una función que ya contiene un valor por defecto en caso de que no se le pase ningún valor cuando la función es invocada.

13. ¿Qué es una variable local y qué una global? ¿Qué es el scope de una variable?

Una **variable local** es una variable que puede ser utilizada dentro de determinado bloque de código, mientras que la **variable global** puede ser utilizada a lo largo de todo el programa. El **scope** de una variable es el alcance que tiene la misma, es decir hasta qué lugar del programa puede ser utilizada.

14. ¿Qué es cohesión y qué acoplamiento?

**Cohesión** es que las funciones que creamos sean independientes unas de otras y se complementen bien. Acoplamiento es la dependencia de una función sobre otra.

15. ¿Python utiliza pasaje por valor o por referencia?

**Python** utiliza pasaje por referencia.

16. ¿Qué es git, qué es github, cómo se relacionan y por qué no son lo mismo?

**Git** es una software de control de versiones, es decir, un software que rastrea los cambios que hacemos en nuestro programa. **GitHub** es una plataforma donde podemos alojar nuestros proyectos **git**, permitiendo la colaboración de otras personas y acceso remoto a nuestros proyectos.

## D - Recursividad

17. ¿Cuál es la utilidad de la recursividad?

Permite **resolver problemas** de forma elegante y a veces, más legible. Algunos problemas son por naturaleza recursivos 

18. ¿En qué parte de la memoria se realiza?

Se realiza en la **pila de llamadas** o **memory stack**.

19. Describir con sus palabras qué entiende por ventajas y desventajas

**Ventajas**: código más legible, resuelve problemas complejos.

**Desventajas**: rendimiento, complejidad para depurar.