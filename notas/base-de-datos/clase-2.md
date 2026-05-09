# DDL (Definición de Datos)

Primero debemos crear una estructura para empezar a trabajar.

## ¿Cómo crear una tabla?

En mayúsculas las palabras reservadas.

`CREATE TABLE tabla`

Luego, (definición de columna [, definición de columna]...
[, definicioón-de-clave-primaria]
[, definición-de-clave-ajena] [, definición-de-clave-ajena]…]);

El nombre de la tabla en mayúsculas y en plural por convención.

**Tablas padre**

```sql
CREATE TABLE PROVEEDORES
(NUMERO INT NOT NULL,
NOMBRE VARCHAR(20) NOT NULL,
DOMICILIO VARCHAR(15) NOT NULL,
LOCALIDAD VARCHAR(12),
PRIMARY KEY (NUMERO));
```

```sql
CREATE TABLE PRODUCTOS
(PNRO INT NOT NULL,
PNOMBRE VARCHAR(20) NOT NULL,
PRECIO INT NOT NULL,
TAMAÑO VARCHAR(20),
LOCALIDAD VARCHAR(12) NOT NULL,
PRIMARY KEY (PNRO));
```

En este caso indicamos las referencias de **NUMERO** y **PNRO** para la **clave compuesta**

```sql
CREATE TABLE PROV_PROD
(NUMERO INT NOT NULL,
PNRO INT NOT NULL,
CANTIDAD INT NOT NULL,
PRIMARY KEY (NUMERO, PNRO),
FOREIGN KEY (NUMERO) REFERENCES PROVEEDORES (NUMERO),
FOREIGN KEY (PNRO) REFERENCES PRODUCTOS (PNRO));
```

## Alterar una tabla

Lo único que podemos alterar es una tabla:

`ALTER TABLE PRODUCTOS ADD COLOR VARCHAR (10);`

## Dar de baja una tabla

`DROP TABLE table;"`

## Crear índices

Cuando creamos un objeto debemos indicar en la **primer letra el tipo de objeto**, por ejemplo:

`CREATE INDEX I_XN ON PROVEEDORES (NUMERO);`

Para alterar un índice, como **solo podemos alterar tablas**, simplemente lo eliminamos y lo volvemos a crear.

## Vistas

Las vistas sirven para mostrar un **recorte de la tabla**, que además podemos limitar qué cosas pueden ver la persona con acceso a la vista. También sirve para **proteger datos sensibles** y **evitar equivocaciones sobre la tabla**.

# DML (Manipulación de Datos)

**SELECT**: consultas  
**UPDATE**: actualizar datos  
**INSERT**: insertar datos  
**DELETE**: borrar datos  

### Ejercicios

Ejercicios desde la pág 23 hasta 26. Copiar la sentencia.