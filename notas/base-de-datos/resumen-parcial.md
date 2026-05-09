# Introducción

**Mysql** es un **sistema de gestión de base de datos** open-source. 
Se encarga de hacer que la información sea persistente y que pueda ser
accedida o manipulada por distintos usuarios.

Hay **dos aspectos** del **diseño de la base de datos** a tener en cuenta:

- Los **datos** deben ser **independientes** de los programas.

- Debe ser posible **explorar** la base de datos **sin necesidad de usar 
un lenguaje de programación**. Para esto existe el lenguaje **SQL (Structured 
Query Language)**

# Componentes de una base de datos

### Información

La información es **integrada y compartida**. Esto quiere decir que puede considerarse como una unificación de archivos y que sus elementos individuales pueden ser compartidos por varios usuarios.

### Equipos

Lugar **donde se alojan las bases de datos**, como servidores, volúmenes de almacenamiento.

### Programas

- Programas de aplicación: permite la interacción entre usuarios y la base de datos.
- Programas de administración: maneja las solicitudes de acceso, la obtención y puesta al día de datos. Esto se hace mediante *software*.

### Usuarios

- DBA (Aministrador de la Base de Datos): se encarga del control general del sistema a nivel técnico:
    - Define el diseño de la base de datos y la vinculación con los usuarios.
    - Define la seguridad e integridad de los datos
    - Practica procedimientos de respalda y recuperación.
    - Supervisión del desempeño y cambios en lo requerimientos

- Analista de sistemas y programador: determinan los requerimientos para los usuarios finales. Escriben los programas que utilizan la BD.

- Usuarios finales: interactúan con el sistema a través de los programas que desarrollan los programadores.

# Características de una base de datos

- Independecia de datos respeto de los programas.
- Disminución de la redundancia.
- Naturaleza autodescriptiva.
- Manejo de múltiples vistas (distintas vistas para distintos usuarios).
- Compacta, rápida y actualizada.
- Posibilidad de aplicar restricción de seguridad.
- Auditoría y recupero.
- Relacionabilidad (podemos relacionar datos de diferentes tablas).

# Conceptos clave

- **Atributo**: así se le llama a las columnas o ítem de datos.
- **Cardinalidad**: es el número de filas que contiene una tabla.
- **Grado de relación**: la cantidad de columnas que tiene una tabla.
- **Dominio**: es el rango de valores atómicos que puede tomar un atributo. Por ejemplo ir de 001 a 999.

Una tabla puede ser de **entidad** o de **interrelación**.

Si es de **entidad** quiere decir que representa un objeto de la vida real como **Alumno** o **Curso**.

Mientras que si es una **interrelación** quiere decir que tenemos una tabla que **conecta** dos o más tablas de entidad, por ejemplo: **Inscripciones** contendra las llaves foráneas compuestas: **ID_ALUMNO**, **ID_CURSO**.

## Tipos de relaciones

- **Relaciones base o reales**: son aquellas que tienen nombre, como las tablas o entidades.

- **Vistas**: está representada dentro del sistema mediante su definición en términos de otras relaciones con nombre. Es una relación derivada.

- **Instantáneas**: También es una relación derivada pero son reales en lugar de virtuales, además de estar representada por su definición en término de otras relaciones con nombre, también tiene sus propios datos almacenados.

- **Relaciones de consulta**: Pueden o no tener nombre. No tienen existencia permanente.

- **Relaciones temporales**: Es una relación con nombre que se destruye, por ejemplo al terminar una sesión.