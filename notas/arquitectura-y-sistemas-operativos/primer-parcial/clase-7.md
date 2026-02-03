# Linux

### Permisos

Para dar permisos a un usuario podemos usar: `chmod u-x archivo`. Esto le da al usuario permiso de ejecución de un archivo. También podemos usar la notación octal (es la que usaremos).

Cuando hacemos `ls -l` cada directorio o archivo tendra esta información, por ejemplo: 

- `drwxrwxrwx` o `-rwxrwxrwx`.
    - d: significa que es un directorio.
    - rwx: r significa **read**, w significa **write**, y x significa **ejecución**.
    - si hay un **-** significa que no tiene tal permiso, por ejemplo `drwxrw-rwx`, significa que el grupo no tiene permiso de ejecución.

- Luego indica la cantidad de enlaces físicos.
- Luego el propietario y grupo al que pertenece el directorio o archivo.
- Finalmente indica el tamaño, fecha y hora (en que fue creado o modificado) y nombre del directorio o archivo.

Por ultimo, el primer rwx indica los **permisos del dueño**, el segundo rwx indica los **permisos del grupo**, y el tercer rwx indica los **permisos de otros usuarios**.

`chmod 755 nombre_archivo` (notación octal) o para hacerlo de forma recursiva: `chmod -R 755 nombre_directorio`. Esto le da permiso al dueño de leer, escribir y ejecutar, y al grupo y a otros usuarios solo permiso de leer y ejecutar.

Para cambiar el propietario y el grupo de un archivo podemos usar: `sudo chown nombre_propietario:nombre_grupo archivo` o para hacerlo de forma recursiva a un directorio `chown -R nombre_propietario:nombre_grupo nombre_dir/`

## ¿Qué es un script?

Es la ejecución de comandos de manera automática. Para ejecutar un script, utilizamos `bash nombre_script`. 

Otra manera de crear un script (es la que usaremos): 

- Creamos el archivo con extensión **.sh** (no es obligatorio, pero si colocamos la extensión todos pueden reconocer que es un script).

- Colocar el **shebang** (#!/bin/bash) al inicio del archivo.

- Para ejecutar, utilizamos `./nombre_script` (antes debemos asignar al usuario permiso de ejecución).