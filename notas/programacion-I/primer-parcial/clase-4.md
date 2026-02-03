# Break

```python
contador = 0

while contador < 5:
    contador += 1

    print(contador)

    seguir = input("¿Quiere continuar? N/S: ")

    if seguir == "N":
        break
```

Dentro del **while** no es muy común usar el break, ya que podemos incluir la condición en el while. Además, esto hace **más legible** nuestro código.

```python
contador = 0
seguir = "S"

while contador < 5 and seguir == "S":
    contador += 1

    print(contador)

    seguir = input("¿Quiere continuar? N/S: ")

```

Dentro de un **while** anidado, el break solo actúa en el while donde está ubicado. Por ejemplo:

```python
# Esto hace un bucle infinito
while True:
    while True:
        print("Prueba")
        break
```

# Validaciones

Verifica que los datos ingresados sean correctos.

```python
clave = int(input("Ingrese su clave: "))

if clave != 619:
    print("Esa no es la clave correcta")
    clave = int(input("Ingrese su clave: "))
```

El **if** solo valida una vez que el dato sea correcto. En cambio, el **while** hace las validaciones las veces que sea necesario.

```python
clave = int(input("Ingrese su clave: "))
contador = 0

while clave != 619 and contador < 5:
    print("Esa no es la clave correcta")
    clave = int(input("Ingrese su clave: "))
    contador += 1

    if contador == 5:
        print("Ingreso demasiadas veces mal la clave, volver a intentar en...")
        # Incluimos demora
```

Otro ejemplo:

```python
contador = 0
acumulador = 0
seguir = "S"

while seguir == "S":
    nota = int(input("Ingrese la nota del alumno: "))
    
    # Validación de rango
    while nota < 1 or nota > 10:
        print("Los valores permitidos son del 1 al 10")
        nota = int(input("Ingrese la nota del alumno: "))

    contador += 1
    acumulador += nota
    promedio = acumulador / contador
    
    seguir = input("¿Quiere continuar agregando notas? S/N")

    # Validando conjuntos
    while seguir != "S" and seguir != "N":
        print("Solo es válido ingresar S o N")
        seguir = input("¿Quiere continuar agregando notas? S/N")

print(promedio)
```