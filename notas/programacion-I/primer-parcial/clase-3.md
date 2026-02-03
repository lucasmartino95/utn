# Estructuras repetitivas

Las **estructuras repetitivas**, permiten repetir una acción o conjunto de acciones varias veces.

## While

Mientras la condición se cumpla, se ejecutará el bloque de código dentro del bucle.

```python
condicion = True

sentencias_a_repetir = int(input("Ingrese la cantidad de veces que quiere que se ejecute el while: "))

while condicion:
    print("Se está ejecutando el while")

    sentencias_a_repetir -= 1
    if sentencias_a_repetir == 0:
        condicion = False
```

### Bucle infinito

Debe haber una instrucción dentro del bucle **que convierta la condición en falso**, de lo contrario estaríamos creando un bucle infinito.

Para detener un bucle infinito, debe suceder algún evento externo, como detener el programa con algún atajo de teclado.

Forma correcta del ejemplo anterior:

```python
sentencias_a_repetir = int(input("Ingrese la cantidad de veces que quiere que se ejecute el while: "))

while sentencias_a_repetir > 0:
    print("Se está ejecutando el while")
    sentencias_a_repetir -= 1
    print(f"Restan {sentencias_a_repetir} iteraciones")
```

Ejemplo usando un acumulador:

```python
limite_diario = 1000

acumulador_gastos = 0

while acumulador_gastos < limite_diario:
    gasto = int(input("Ingrese el gasto realizado: "))

    acumulador_gastos += gasto
    if acumulador_gastos > limite_diario:
        print(f"Ya gastó ${acumulador_gastos} y excedió el límite")
    else:
        print(f"Lleva gastados ${acumulador_gastos}")
```

El código anterior es redundante. Se puede escribir mejor de esta manera:

```python
limite_diario = 1000

acumulador_gastos = 0

while acumulador_gastos < limite_diario:
    print(f"Lleva gastados ${acumulador_gastos}")
    gasto = int(input("Ingrese el gasto realizado: "))
    acumulador_gastos += gasto

print(f"Ya gastó ${acumulador_gastos} y excedió el límite")
```
