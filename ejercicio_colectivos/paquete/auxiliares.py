def validar_linea(linea: int, lineas: list) -> bool:

    for i in range(len(lineas)):
        if linea == lineas[i]:
            return True
        

def validar_coche(coche: str, coches: list) -> bool:
    for i in range(len(coches)):
        if coche == coches[i]:
            return True
        