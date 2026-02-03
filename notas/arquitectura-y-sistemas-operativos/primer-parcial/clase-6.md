## Crear directorios

Para crear directorios, podemos usar ```mkdir```. Por ejemplo

```bash
mkdir -p {dir1, dir2}/subdir{1..3}
```

Otro ejemplo

```bash
mkdir -p {dir1,dir2}/{subdir1,subdir2,subdir3}
```

Si luego utilizamos ```tree``` nos mostrará la estructura de los directorios que creamos.

## Ver archivos

Para ver archivos desde la terminal, podemos usar el caomando `cat`. Por ejemplo: `cat /etc/passwd`

## Buscar cadenas dentro de un archivo

Podemos usar el comando `grep`. Por ejemplo: `grep -i vagrant /etc/passwd`. La `-i` significa que no distinga entre mayúsculas y minúsculas.

## Grupos y usuarios

Los grupos en Linux, se usan para administrar los permisos que tiene un usuario sobre los archivos.

Para agregar un grupo, usamos `groupadd nombre_del_grupo`. Luego podemos crear un usuario y añadirlo al grupo que creamos: `useradd -m -s /bin/bash -c "Usuario lucas" -G nombre_del_grupo lucas`

### Borrar un usuario

`userdel nombre_de_usuario`

### Modificar un usuario

`usermod -s /bin/sh nombre_del_usuario`
