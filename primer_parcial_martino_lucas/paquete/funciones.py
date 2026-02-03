def cargar_existencias(depositos: list,
                       materiales: list,
                       existencias: list,
                       deposito: str,
                       material: str,
                       cantidad: int) -> list:

    match deposito:
        case "Haedo":
            fila = 0
        case "Tigre":
            fila = 1
        case "San Martín":
            fila = 2
        case "Florencio Varela":
            fila = 3
        case "Mercedes":
            fila = 4
        case "Ezeiza":
            fila = 5
        case "José León Suarez":
            fila = 6

    for i in range(len(materiales)):
        if material == materiales[i]:
            existencias[fila][i] += cantidad
            print(existencias)


def calcular_cantidad_total_elementos(existencias: list,
                                      deposito: str) -> str:

    match deposito:
        case "Haedo":
            fila = 0
        case "Tigre":
            fila = 1
        case "San Martín":
            fila = 2
        case "Florencio Varela":
            fila = 3
        case "Mercedes":
            fila = 4
        case "Ezeiza":
            fila = 5
        case "José León Suarez":
            fila = 6

    suma = 0

    for i in range(len(existencias) - 1):
        suma += existencias[fila][i]
    
    print(f"La cantidad total de elementos del deposito {deposito}, es: {suma}")


def retornar(depositos: list,
             existencias: list,
             materiales: list,
             material_minimo: bool = True):
    
    if material_minimo:

        deposito = input("Calcula el material que almacenó menos elementos del deposito: ")

        match deposito:
            case "Haedo":
                fila = 0
            case "Tigre":
                fila = 1
            case "San Martín":
                fila = 2
            case "Florencio Varela":
                fila = 3
            case "Mercedes":
                fila = 4
            case "Ezeiza":
                fila = 5
            case "José León Suarez":
                fila = 6
                
        for i in range(len(existencias[fila])):

            if i == 0:
                minimo = existencias[fila][i]
                indice_minimo = i
            else:
                if minimo > existencias[fila][i]:
                    minimo = existencias[fila][i]
                    indice_minimo = i

        print(f"En el depósito {deposito}, el material con menor cantidad de elementos es: {materiales[indice_minimo]}")
        return materiales[indice_minimo]
    
    else:
        suma_lista = [0, 0, 0, 0, 0, 0, 0]

        for i in range(len(existencias)):
            for j in range(len(existencias[i])):
                suma_lista[i] += existencias[i][j]

        for i in range(len(suma_lista)):

            if i == 0:
                maximo = suma_lista[i]
                indice_maximo = i
            else:
                if maximo < suma_lista[i]:
                    maximo = suma_lista[i]
                    indice_maximo = i
        
        print(f"El depósito con mayor cantidad de materiales es: {depositos[indice_maximo]}")


def obtener_recaudacion(depositos: list,
                        existencias: list) -> None:

    suma_lista = [0, 0, 0, 0, 0, 0, 0]
    
    for i in range(len(existencias)):
        for j in range(len(existencias[i])):
            suma_lista[i] += existencias[i][j]
    
    for i in range(len(suma_lista)):
        match i:
            case 0:
                suma_lista[i] *= 10
            case 1:
                suma_lista[i] *= 13    
            case 2:
                suma_lista[i] *= 15
            case 3:
                suma_lista[i] *= 17   
            case 4:
                suma_lista[i] *= 20
            case 5:
                suma_lista[i] *= 18
            case 6:
                suma_lista[i] *= 8
    
    for i in range(len(suma_lista)):
        if i == 0:
            maxima_recaudacion = suma_lista[i]
            indice_max_recaudacion = i
        else:
            if maxima_recaudacion < suma_lista[i]:
                maxima_recaudacion = suma_lista[i]
                indice_max_recaudacion = i

    print(f"El depósito que tiene mayor recaudación es: {depositos[indice_max_recaudacion]}")


def obtener_deposito_mas_50000(existencias: list) -> None:
    
    suma_lista = [0, 0, 0, 0, 0, 0, 0]

    for i in range(len(existencias)):
        for j in range(len(existencias[i])):
            suma_lista[i] += existencias[i][j]

    cantidad_depositos_mas_50 = 0

    for i in range(len(suma_lista)):
        if suma_lista[i] > 50000:
            cantidad_depositos_mas_50 += 1

    print(f"La cantidad de depositos que almacenaron más de 50.000 elementos son: {cantidad_depositos_mas_50}")


def obtener_porcentaje(existencias: list,
                       materiales: list) -> None:
    pass