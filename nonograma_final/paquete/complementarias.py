def validar_ingreso(fila_o_columna: int,
                    mensaje: str) -> None:

    while fila_o_columna > 4:
        
        fila_o_columna = int(input(mensaje))

    return fila_o_columna