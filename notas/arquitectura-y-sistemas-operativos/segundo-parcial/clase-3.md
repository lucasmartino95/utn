# Docker

**Docker** es un software de código abierto, multiplataforma. Nos permite virtualizar aplicaciones, es decir, ejecutar nuestras aplicaciones dentro de un contenedor que tendrá todas las dependencias y librerías necesarias.

Es como una **máquina virtual** pero mucho más veloz. Ademas, Docker no necesita ningún hipervisor. Tiene un **daemon** que ejecuta los comandos que ingresamos.

Para ejecutar una aplicación dentro de un contenedor, necesitamos **construir una imagen**.
Esta imagen es la **preparación** para ejecutar la aplicación. Es la aplicación en estado estático

## Registry

Es una plataforma en la web, similar a GitHub. **DockerHub** nos permite guardar las imágenes que creamos. Luego podemos descargarlas para usarlas en cualquier otra computadora. En el **registry** solo podemos guardar nuestras aplicaciones en estado estático, es decir las imágenes.

En **DockerHub** hay imágenes oficiales de Docker e imágenes que construyen los usuarios y las suben a **DockerHub**.

## Límites

Docker no puede manejar demasiados contenedores, para eso existen **orquestadores** como **Kubernetes**.
