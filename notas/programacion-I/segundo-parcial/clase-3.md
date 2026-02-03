# Archivos

Utilizamos **archivos** para que la información de nuestro programa sea permanente.

Los archivos pueden ser de **texto** o **binario**.

Los archivos de **texto** podemos **abrirlos y modificarlos**, como un archivo .txt o .csv. En cambio, los **archivos binarios** no se pueden interpretar, como una imagen o un sonido.

### Pasos para trabajar con archivos de texto

1. **Apertura**

2. **Lectura**

3. **Escritura**

4. **Cierre**

## CSV

**CSV (Comma Separated Values)** es un formato que almacena datos en tabla, donde cada línea representa una fila y los valores dentro de cada fila están separado por comas.

# Programación funcional

Es un **estilo de programación** que utiliza funciones como unidad básica de código.

Para que un lenguaje sea funcional, las funciones deben ser tratadas como **ciudadanos de primera clase**. Es decir, que el lenguaje nos permita que las funciones sean objetos, como un string o un entero.

```python
def restar_2(num: int) -> int:
    return num - 2


objeto_funcion = restar_2

print(objeto_funcion(5))
```

## Características

- **Funciones puras**: depende solo de sus parámetros de entrada y no tiene efectos secundarios.

- **Hacer el código más declarativo**: se enfoca más en qué se hace más que en cómo se hace.

- **Funciones de orden superior**: son funciones que reciben otra función como parámetro.

- **Expresiones en lugar de instrucciones**: en lugar de usar bucles y condicionales, se favorece el uso de expresiones y combinaciones de funciones.
