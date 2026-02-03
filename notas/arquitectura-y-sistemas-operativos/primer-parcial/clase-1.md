# Introducción

Una computadora es un **dispositvo electrónico** capaz de procesar enormes secuencias de instrucciones muy velozmente.

Las computadoras eran utilizadas para fines específicos y ocupaban grandes espacios físicos. Con el avance de la electrónica las computadoras **se volvieron más pequeñas y más poderosas**, también más accesibles economicamente ya que el coste de producción también se redujo.

Y el uso de las computadoras se volvió **más generalizado**.

Toda computadora está formada por dos componentes: **hardware** y **software**.

## Hardware

Es la parte física. Está **compuesto** por el equipo y los dispositivos que conforman o están asociados a él.

## Software

Es la parte lógica. Son los **programas, procedimientos o datos**, asociados con el procesamiento de datos.

#### Programa
Es un conjunto de instrucciones, escritas en un lenguaje de programación, que le indica a la computadora cómo realizar una tarea específica.

### Clasificación de software

#### Software libre

El software libre surge por un proyecto llamado **GNU**. Su fundador [Richard Stallman](https://es.wikipedia.org/wiki/Richard_Stallman), quería que **GNU** se pareciera a **UNIX**. Pero no creó el *kernel* del sistema operativo, sino que usó **Linux**. Por eso se escribe **GNU/Linux** para referirse a una distribución comúnmente llamada **Linux**.

El código de software libre se puede **copiar y distribuir**. También, podemos utilizar los programas de software libre para cualquier fin.

#### Software propietario

El código del software propietario es **cerrado**, o sea que **no se puede copiar o distribuir**. Tampoco podemos modificar su funcionamiento. Un ejemplo es **Windows o Mac**

## Arquitectura actual de computadoras

Las computadoras convencionales siguen la arquitectura propuesta a principio de los años 40 por [Von Neumann](https://es.wikipedia.org/wiki/Arquitectura_de_Von_Neumann):

- El procesador central o CPU.
- La memoria en la que residen datos y programas.
- Los dispositivos de entrada y salida o periféricos.

Toda la información viaja a través de los distintos componentes en **sistema binario**, es decir con ceros y unos. También se puede referenciar el cero con "apagado" y el uno con "encendido".

## Arquitectura de los sistemas operativos

### Kernel

El **sistema operativo** está compuesto por capas.

El **Kernel o núcleo** es la capa más cercana al **hardware** y cumple las funciones más importantes. Es el que interactua con el **hardware**. Le indica cómo debe manejar ciertos aspectos, como por ejemplo cómo manejar la memoria, cómo manejar la entrada y salida de datos, cómo manejar el sistema de archivos. Es un **software de base**.

Todo esto lo puede hacer mediante **controladores de hardware, gestión de procesos y gestión de memoria**.

#### Tipos de kernel

##### Monolítico

Todos los servicios, gestión de procesos y memoria **se ejecutan dentro del kernel**. Esto garantiza un muy buen rendimiento del sistema.

##### Microkernel

**Solo incluye las funciones más básicas**, el resto de servicios del sistema operativo se ejecutan en procesos separados en el espacio de usuario.

##### Híbrido

Es una **combinación** del kernel monolítico y el microkernel.

### Llamadas al sistema

Cada vez que hacemos clic o ejecutamos un comando en la shell, hacemos una **llamada al sistema operativo**, el cual deriva la llamada a distintos procesos internos para hacer una devolución.

#### GUI / Shell

Podemos interactuar con el sistema operativo a través de una [GUI (Graphical User Interface)](https://es.wikipedia.org/wiki/Interfaz_gr%C3%A1fica_de_usuario) o una [línea de comandos](https://es.wikipedia.org/wiki/L%C3%ADnea_de_comandos_de_Windows). Comúnmente la línea de comandos es más poderosa que una GUI, es decir, podemos hacer operaciones más avanzadas.

## Procesador

Es el responsable de **ejecutar programas**.

El procesador tiene una **unidad de control** que es la responsable de procesar cada instrucción y transferir información entre la **unidad aritmética lógica (ALU en inglés)** y la **memoria RAM**.

La **unidad aritmética lógica** se encarga de realizar operaciones aritméticas, operaciones lógicas y operaciones de comparación. Recibe los datos de los registros del procesador, procesa las instrucciones y devuelve los resultados.

Los **registros** del procesador son un tipo de memoria interna. Es donde se almacena momentaneamente algún dato específico. Por ejemplo, guarda la dirección de la celda de memoria RAM en donde se debe ejecutar una instrucción.

### Un procesador está compuesto por

#### Núcleos

Un núcleo es un **bloque que ejecuta instrucciones**.

Podemos tener uno o más núcleos en nuestro procesador. Esto quiere decir que si tenemos por ejemplo cuatro núcleos, podemos ejecutar un programa en cada núcleo. Esto se llama **multitarea**.

#### Hilos

Los hilos son una versión virtual de un núcleo. Podemos definir un hilo de procesamiento como el **flujo de control de datos de un programa**. Es un medio que permite administrar las tareas de un procesador y de sus diferentes núcleos de una forma más eficiente. **Divide la tarea en porciones**, lo que quiere decir que cada hilo se encarga de una parte concreta de dicho programa. Estas porciones se llaman **subprocesos o threads**.

Por cada núcleo existen dos hilos, aunque puede haber excepciones.

Se puede decir que los hilos **convencen** al usuario y a la PC de que se pueden realizar más tareas al mismo tiempo.

Para utilizar múltiples núcleos y sus hilos **es necesario que los programas se comuniquen con cada uno de los núcleos**.

#### Reloj o clock

El reloj o clock es un **componente del microprocesador** que emite pulsos eléctricos a intervalos constantes llamados ciclos, estos ciclos **marcan el ritmo** para todas las operaciones que realiza el procesador. La **velocidad de reloj** indica cuántos ciclos de procesamiento por segundo puede ejecutar una CPU teniendo en cuenta todas sus unidades de procesamiento (núcleos).

**Esta velocidad se mide en GHz**, los cuales  se traducen de esta manera, por ejemplo:

3.7GHz = 3.700 millones de instrucciones por segundo.

### Overlock

El overlock es una técnica utilizada para **aumentar la frecuencia de reloj** de un componente electrónico, en este caso del procesador.

Una desventaja de utilizar esta técnica es que **aumenta el calor que emite el procesador**, ya que lo estamos forzando a trabajar más velozmente. También **reduce la vida útil del componente**.

## Memoria RAM

La memoria RAM está hecha de celdas, donde cada celda está identificada con un número. Es donde **se guardan los datos e instrucciones de nuestro programa** para que luego el procesador lo ejecute.

## Dispositivos de entrada y salida

El fin último de una computadora es ingresarle datos, que haga el procesamiento
y nos devuelva un resultado. Para esto, contamos con dispositivos de entrada y de salida.

Dispositivos de entrada:

- Teclado
- Mouse
- Micrófono

Dispositivos de salida:

- Monitor
- Auriculares
- Impresora

Dispositivos de entrada y salida:

- Pendrive
- Disco rígido o de estado sólido
- Pantalla táctil