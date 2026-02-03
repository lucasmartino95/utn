def validate_number(numero: int|float,
                    mensaje_error:str,
                    minimo: int,
                    maximo: int,
                    reintentos: int) -> int|float|None:

    bandera = True

    limite = 0

    while bandera:
        if numero >= minimo and numero <= maximo:
            return numero
        else:
            # Le resto 1 a reintentos para que se tome
            # en cuenta el primer input que está fuera
            # del while dentro de la función get_int o get_float
            if limite < (reintentos - 1):
                print(mensaje_error)

                if type(numero) == int:
                    numero: int = int(input("Ingresa un número: "))
                else:
                    numero: float = float(input("Ingresa un número: "))
                limite += 1
            else:
                return None


def validate_length(cadena: str,
                    mensaje_error: str,
                    longitud: int,
                    reintentos: int) -> str|None:
    
    bandera = True

    limite = 0

    while bandera:
        if len(cadena) != longitud:
            # Le resto 1 a reintentos para que se tome
            # en cuenta el primer input que está fuera
            # del while
            if limite < reintentos - 1:
                print(mensaje_error)
                cadena: str = input(f"Escribe algo de {longitud} caracteres: ")
                limite += 1
            else:
                return None
        else:
            return cadena