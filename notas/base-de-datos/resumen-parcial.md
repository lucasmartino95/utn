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
