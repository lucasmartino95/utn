from paquete.funciones import *

salones = [0, 0, 0]

puerto_madero = ["Cumpleaños", 0, "Casamientos", 0, "Fiestas de 15", 0,
                 "Bodas de oro", 0]

palermo = ["Cumpleaños", 0, "Casamientos", 0, "Fiestas de 15", 0,
                 "Bodas de oro", 0]

san_telmo = ["Cumpleaños", 0, "Casamientos", 0, "Fiestas de 15", 0,
                 "Bodas de oro", 0]

while True:
    opcion = mostrar_menu_opciones()
    if opcion == 8:
        break
    else:
        match opcion:
            case 1:
                evento = input("Ingresa un evento: ")
                salon = input("Ingresa un salón: ")
                cargar_evento(puerto_madero, palermo, san_telmo, salones, evento, salon)
                seguir = input("Quieres cargar otro evento? (S/N): ")
                while seguir == "S":
                    evento = input("Ingresa un evento: ")
                    salon = input("Ingresa un salón: ")
                    cargar_evento(puerto_madero, palermo, san_telmo, salones, evento, salon)
                    seguir = input("Quieres cargar otro evento? (S/N): ")
            case 2:
                calcular_total_fiestas_por_salon(salones)
            case 3:
                consultar_evento_mas_realizado_por_salon(puerto_madero, palermo, san_telmo)