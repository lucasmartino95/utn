# Modulos

A medida que los programas crecen, se hace necesario **separar el código** en distintas partes que hagan una tarea específica cada una.

## Main

Es el archivo donde utilizaremos las funciones, de los distintos módulos de nuestro programa.

```python
""" Supongamos que tenemos un archivo llamado modulo_alumnos
"""
import modulo_alumnos

modulo_alumnos.imprimir_nombre("Lucas")
```

Otras maneras de importar

```python
from modulo_alumnos import imprimir_nombre

imprimir_nombre("Lucas")
```

```python
from modulo_alumnos import imprimir_nombre, devolver_promedio

imprimir_nombre("Lucas")
devolver_promedio(8, 2)
```

```python
from modulo_alumnos import *

imprimir_nombre("Lucas")
devolver_promedio(8, 2)
```

# Paquetes

Las funciones se agrupan en módulos, y los módulos en paquetes.

Por ejemplo

```python
# Dentro de un archivo __init__.py en la carpeta utn

from .alumnos import *
from .docentes import *
```

```python
# Dentro del archivo main.py
from utn import *
```

# Control de versiones

**Git** es un software de control de versiones. Permite rastrear los cambios que hay en el desarrollo de un software. Para ello, git crea un repositorio en nuestra máquina local.

[GitHub](https://github.com/) es una plataforma que permite alojar repositorios [git](https://git-scm.com/) en la nube, para acceder a ellos remotamente permitiendo colaborar en proyectos de software.