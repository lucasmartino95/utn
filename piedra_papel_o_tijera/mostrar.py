def mostrar_elemento(eleccion: int) -> str:

    match eleccion:
        case 1: 
            return "Piedra"
        case 2:
            return "Papel"
        case 3:
            return "Tijera"