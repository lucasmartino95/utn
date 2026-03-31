# Introducción

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

## Componentes de una base de datos

### Información

Es **integrada y compartida**. La base de datos puede considerarse como una unificación de varios archivos de datos, evitando redundancia. Compartida quiere decir que los **elementos de la base de datos** pueden comparirse por varios usuarios distintos.