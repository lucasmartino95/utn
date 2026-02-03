# Ejemplo de juego

```python

# En un módulo: paquete.complementarias.py
def mostrar_opciones(mensaje: str) -> str:

    print("1 - Jugar ahorcado")
    print("2 - Ranking")
    print("3 - Salir del juego")

    opcion = input(mensaje)

    return opcion


def validar_letra(caracteres: str) -> bool:

    control = False

    if len(caracteres) != 1:
        print("Debe ingresar una sola letra")
    elif caracteres.isalpha() == False:
        print("Debe ingresar una letra. No son válidos otros caracteres")
    else:
        control = True

    return control


def controlar_letra_ingresada(caracter: str, lista_caracteres: list) -> bool:

    for letra in lista_caracteres:
        if letra == caracter
            print("Esa letra ya fue ingresada")
            return True
    
    return False

# En un módulo: paquete.logica.py
def seleccionar_palabra(ruta: str) -> str:
    
    palabras = leer_archivo(ruta)

    if len(palabras) > 0:
        palabra = choice(palabras)
    else:
        print("El archivo está vacío")
    
    return palabra


# En un módulo: paquete.manejo_archivos.py
def leer_archivos(ruta: str, modo: int = 1, separador: str = ",") -> list:
    lista_retorno = []

    with open(ruta, encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            valores = linea.split(separador)

            if modo == 1:
                lista_retorno.append(valores[0])
    return lista_retorno


# Archivo main.py
jugar = True

ruta_palabras = "archivos/palabras.csv"

while jugar:
    opcion = mostrar_opciones("Ingrese tarea que desea realizar") # Evita repetir código

    # Validación
    while opcion.isdigit() == False:
        opcion = mostrar_opciones("Ingresar un número válido: ")

    opcion = int(opcion)

    match opcion:
        case 1:
            caracteres_seleccionados = []
            palabra_seleccionada = seleccionar_palabra(ruta_palabras)
            copia_palabra = "_" * len(palabra_seleccionada)

            print()
            print(copia_palabra)
            print()

            letra = input("Ingresar una letra: ")

            while validar_letra(letra) == False:
                letra = input("Ingrese una letra: ")

            while controlar_letra_ingresada(letra, caracteres_seleccionados):
                while validar_letra(letra) == False:
                    letra = input("Ingrese una letra: ")
                        
            for i in range(len(palabra_selecionada)):
                pass


        case 2:
            pass
        case 3:
            jugar = False
        case _:
            print("Opción no válida")
```