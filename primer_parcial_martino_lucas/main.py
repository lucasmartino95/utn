from paquete.funciones import *


depositos = ["Haedo", "Tigre", "San Martín", "Florencio Varela", "Mercedes",
             "Ezeiza", "José León Suarez"]
        
        
materiales = ["Cemento", "Ladrillos", "Cal", "Arena", "Varillas de acero",
              "Pintura"]

existencias = [[0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0]]


while True:

    print("Menú")

    print("[1] Cargar existencias")
    print("[2] Calcular por cada depósito la cantidad total de elementos " \
    "almacenados entre todos los materiales")
    print("[3] Retornar el nombre del material que almacenó menos elementos " \
    "en cada depósito")
    print("[4] Retornar el depósito que almacenó la máxima cantidad de " \
    "elementos de cada material")
    print("[5] Depósito con mayor recaudación")
    print("[6] Cantidad de depósitos que hayan almacenado más de 50.000 " \
    "elementos entre los 5 materiales")
    print("[7] Porcentaje de elementos de cada material sobre el total de " \
    "elementos almacenados. Mostrar el nombre del elemento con " \
    "el máximo porcenaje")
    print("[8] Generar un informe con la recaudación de cada depósito, " \
    "ordenada de mayor a menor")
    print("[9] Salir")

    opcion = int(input("Ingresa la tarea a realizar: "))

    if opcion == 9:
        break
    else:
        match opcion:
            case 1:

                print("Cargar existencias")

                deposito = input("Ingresa depósito a cargar: ")
                material = input("Ingresa material: ")
                cantidad = int(input("Ingresa cantidad: "))
            
                cargar_existencias(depositos, materiales, existencias,
                                deposito,
                                material,
                                cantidad)
            case 2:
                deposito = input("Calcula la cantidad total de elementos del deposito: ")
                calcular_cantidad_total_elementos(existencias,
                                                  deposito)
            case 3:
                retornar(depositos,
                         existencias,
                         materiales)
            case 4:
                retornar(depositos,
                         existencias,
                         materiales,
                         False)
            case 5:
                obtener_recaudacion(depositos,
                                    existencias)
            case 6:
                obtener_deposito_mas_50000(existencias)
            case 7:
                obtener_porcentaje(existencias,
                                   materiales)