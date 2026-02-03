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