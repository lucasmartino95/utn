Parcial martes 12/05

# Catálogo

Es el **compendio de todos los objetos** que forman la base de datos, es decir, columnas, índices, llaves foráneas. Estos son **metadatos**.

Se puede asemejar a un diccionario de datos. **Otorga información** a los usuarios de la base de datos y principalmente al administrador.

Algunas vistas de catálogo son:

- **SYSTABLES**
- **SYSCOLUMNS**
- **SYSINDEXES**
- **SYSVIEWS**

## Integridad relacional

Lo que busca es que los datos de la base de datos **no genere errores**. Nos permite trabajar con cierta estructura. Lo hacemos aplicando **restricciones**, o sea *constraints*.

`Documeto INT CONSTRAINT uk_documento UNIQUE`

- uk_constraint: **u** es de Unique y **k** es de constraint

Se consideran también **reglas de negocio**.

## Habilitar / deshabilitar constraints

Un flujo de trabajo común es cuando tenemos **dos tablas separadas**, y en una tenemos email del cliente y en la otra teléfono y las queremos unir:

1. Deshabilitamos las *constraints*
2. Unimos las tablas
3. Luego volvemos a habilitar las *constraints*