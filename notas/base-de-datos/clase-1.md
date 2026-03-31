# Introducción

## Unidad 1
Las clases son **teóricas y prácticas**. Antes del primer parcial, hay que entregar
los ejercicios una semana antes (la práctica).

Un **sistema de base de datos** es un sistema computarizado cuyo objetivo es mantener
la información centralizada y hacer que esté disponible cuando se la solicite.

Los **datos** deben ser independientes de los programas. Para acceder a estos datos, podemos usar **SQL (Structured Query Language)**.

Las **bases de datos** están compuestas por **objetos**, por ejemplo:

- Table
- View
- Index
- Store
- Procedure
- Trigger

Para **manipular estos objetos** hay cuatro vías, utilizando estas
palabras reservadas:

- **Modifican la estrutura**  
DDL (Data Definition Language)
    - Create  (todos los objetos de la BD)
    - Alter (table)
    - Drop (todos los objetos de la BD)

- **No modifican la estructura**  
DML (Data Manipulation Language)
    - SELECT
    - UPDATE
    - INSERT
    - DELETE

- **DCL (Data Control Language)**
    - GRANT (otorgar permisos)
    - REVOKE (revocar permisos)

- **TCL (Transaction Control Language)**
    - COMMIT
    - ROLLBACK

### Componentes de una base de datos

#### Información

Es **integrada y compartida**. La base de datos puede considerarse como una unificación de varios archivos de datos, evitando redundancia. Compartida quiere decir que los **elementos de la base de datos** pueden comparirse por varios usuarios distintos.

#### Equipos

Servidores de la base de datos.

#### Programas

- Programas de aplicación: interacción entre los usuarios y la base de datos.
- Programas de administración (SGDB): maneja las solicitudes de acceso a la base de datos, la obtención y puesta al día de los datos.

#### Usuarios

- Administrador de base de datos
- Analista de sistemas y programador de aplicaciones
- Usuarios finales

### Conceptos

**Auditoria**: es una forma de registrar eventos, como alguien que borró o cambió un dato de la base de datos.

**Recupero**: a medida que la base de datos se actualiza, también vamos guardando los cambios por si necesitamos recuperar algún dato.

**Relacionabilidad**: los datos podrán ser utilizados o explorados de manera flexible, con diferentes caminos de acceso, gracias a su relación incluida de datos.

## Unidad 2

Una base de datos relacional es aquella que los usuarios la perciben como un conjunto de tablas.

### Tipos de relaciones

**Vistas**: obtener los datos de un determinado campo.

**Instantáneas (snapshots)**: toma una foto de la base de datos y hace una copia íntegra sin que el usuario note que estoy copiando la base de datos. Con esto puedo hacer pruebas o *backup*.

A diferencia de la vista, tiene los **datos reales** de la base, no solo un recorte.

**Resultado de consultas**: pueden o no tener nombre. No tienen existencias persistente

**Relaciones temporales**: es una relación con nombre que se destruye. Por ejemplo al terminar una sesión activa

Para darme cuenta si una tabla es una **entidad o interrelación**, puedo fijarme en si la **primary key** es compuesta. O también puedo fijarme en el nombre de la tabla. O también revisar si la tabla me da un dato extra que no corresponda a su nombre.

### Ejemplo de interrelación

|Legajo | Materia | Nota |
|---|---|---|
| 6097 | Matemática | 7  |

En este caso, los campos que identifican la nota del alumno es la **primary key** compuesta: legajo y materia.