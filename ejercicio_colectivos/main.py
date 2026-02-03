from paquete.funciones import *
from paquete.auxiliares import *

lineas = [150, 155, 158]

coches = ["ZLJ 102", "TNM 500", "DGE 123", "PRE 230", "UNI 405",
          "RTP 305", "DMN 206", "TRV 207", "NIN 304", "VXZ 111",
          "TRQ 402", "QRT 404", "MNE 555", "KLO 400", "INF 103"]

legajos = [100, 102, 104, 106, 108,
           110, 112, 114, 116, 118,
           120, 122, 124, 126, 128]

recaudaciones = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

while True:
    
    print("Menú de opciones")
    print("[1] Cargar planilla de recaudación")
    print("[2] Mostrar la recaudación de cada línea y coche")
    print("[3] Calcular y mostrar la recaudación por línea")
    print("[4] Calcular y mostrar la recaudación por coche")
    print("[5] Calcular y mostrar la recaudación total")
    print("[6] Salir del programa")
    
    opcion = int(input("Elige una opción: "))

    match opcion:
        case 1:
            legajo = int(input("Ingresa tu número de legajo: "))
            for i in range(len(legajos)):
                if legajo == legajos[i]:
                    print("Legajo válido, ahora ingresa los siguientes datos")

                    linea = int(input("Ingresa la línea con la cual viajaste: "))
                    
                    if validar_linea(linea, lineas):
                        print("Línea correcta, continúa")
                    else:
                        print("Línea incorrecta")
                        break

                    coche = input("Ingresa el coche con el cual viajaste: ")
                    
                    if validar_coche(coche, coches):
                        print("Coche correcto, continúa")
                    else:
                        print("Coche incorrecto")
                        break
    
                    recaudacion = int(input("Ingresa la recaudación: $"))
                    cargar_planilla(linea,
                                    coche,
                                    coches,
                                    recaudacion,
                                    recaudaciones)
                    print("Planilla cargada")
        case 2:
            mostrar_recaudacion(recaudaciones)
        case 3:
            mostrar_recaudacion_por_linea(recaudaciones)
        case 4:
            coche = input("Ingresa el coche con el cual viajaste: ")
            if validar_coche(coche, coches):
                print("Coche correcto, continúa")
            else:
                print("Coche incorrecto")
                break
            mostrar_recaudacion_por_coche(coche, coches, recaudaciones)
        case 5:
            mostrar_recaudacion_total(recaudaciones)
        case 6:
            break