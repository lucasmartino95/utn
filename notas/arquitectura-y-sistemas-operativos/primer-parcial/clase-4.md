# Sistemas operativos

## Gestión de procesos

El **sistema operativo** crea un **bloque de control** que es asignado a la aplicación. En ese bloque se guarda toda la información referida a esa aplicación:

- **Estado actual del proceso**
- **Identificador del proceso**
- **Prioridad del proceso**
- **Ubicación de memoria y recursos utilizados**

Hay muchos programas que son ejecutados sin que el usuario los solicite. Por ejemplo, un antivirus.

Otros procesos, que son ejecutados en **segundo plano**, son conocidos como demonios.

### Hilos

Los hilos son **subprocesos** dentro de un mismo programa. Para eso, el programa debe estar preparado. El sistema operativo, cuando ve un programa, revisa si tiene hilos. Entonces, descompone el programa en pequeñas partes.

Un ejemplo son los procesadores de texto. Si abrimos un libro de trescientas páginas, tendremos un **hilo principal** que atiende las inteacciones como bajar de página. Otro hilo, actúa como corrector ortográfico.

### Estados de un proceso

1. **Inicio**: Se crea el proceso.

2. **Listo**: Espera a ser ejecutado. No hace uso del procesador.

3. **Ejecutando**: Uso real del procesador en un determinado instante. Cuando se interrumpe, vuelve al estado de listo.

4. **Finalizado**: El sistema operativo borra el bloque de control de proceso y libera el espacio de memoria que le había asignado.

- **Bloqueado**
    - Cuando se solicita acceder a un periférico de entrada y salida, se bloquea el proceso hasta que esté lista la respuesta. Entonces vuelve al estado de listo.

Estos pasos son conocidos como **transiciones**. Para el procesador es indistinto si está ejecutando un proceso u otro. Solo ejecuta las instrucciones de cada proceso.

### Planificador

Garantiza que todos los procesos se ejecuten en un orden, revisando la prioridad que tienen. Esto es para hacer un uso **más eficiente** del procesador.

## Gestión de memoria

A cada proceso se le debe asignar un espacio en **memoria RAM**. Esta memoria es insuficiente para almacenar todos los procesos que se ejecutan en el sistema operativo, entonces crea una memoria virtual, la cual utiliza espacio del disco duro.

### Controlador de memoria virtual

Intercambia la información del disco duro a la memoria RAM.

- **Paginación**: Divide la memoria RAM y el almacenamiento secundario (disco) en bloques de tamaño fijo. No genera fragmentación de la memoria RAM.

- **Segmentación**: No divide a la memoria RAM en espacios iguales. En cambio, divide al proceso en las distintas partes que tiene el código. Por ejemplo agrupa las instrucciones por un lado, la asignación de variables por otro lado.

- **Swapping** (Linux): Utiliza un espacio de disco como la extensión de memoria RAM. Es un espacio definido cuando instalamos el sistema operativo. Luego se puede agrandar o achicar.

Notar que tanto la paginación como la segmentación utilizan espacio en disco como memoria virtual.

### Memoria caché

Es donde se guardan los procesos que son **ejecutados habitualmente**. Esta memoria es mucho más rápida que la memoria RAM y está ubicada dentro del procesador.