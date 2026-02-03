from Validate import *

def get_int(mensaje: str) -> int:

    print(mensaje)

    numero: int = int(input("Ingresa un número: "))

    return numero
            

def get_float(mensaje: str) -> float:

    print(mensaje)

    numero: float = float(input("Ingresa un número: "))

    return numero
    

def get_string(longitud: int) -> str:

    cadena: str = input(f"Escribe algo de {longitud} caracteres: ")

    return cadena


entero = get_int("NÚMERO ENTERO")

print(validate_number(entero,
                "Número inválido",
                1,
                10,
                3))

numero_decimal = get_float("NÚMERO DECIMAL")

print(validate_number(numero_decimal,
                "Número inválido",
                1,
                10,
                3))

print("ESCRIBE UN TEXTO")

longitud = int(input("Escribe la longitud del texto que quieres ingresar: "))

texto = get_string(longitud)

print(validate_length(texto, "Texto inválido", longitud, 3))