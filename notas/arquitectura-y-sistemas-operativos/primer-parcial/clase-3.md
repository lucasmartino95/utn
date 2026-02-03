# Virtualización

Es una técnica para crear máquinas virtuales dentro de un equipo físico real.

Cada una de estas máquinas que podemos crear, pueden tener **sistemas operativos diferentes** y **son independientes** unas de otras.

Podemos utilizar máquinas virtuales para probar cosas.

Para virtualizar, sobre el sistema operativo de nuestra máquina, instalamos un software llamado [hipervisor](https://www.redhat.com/es/topics/virtualization/what-is-a-hypervisor). Por ejemplo, VirtualBox. Este software nos permite **configurar el hardware de nuestra máquina virtual**.

### Hipervisor de tipo 1 y tipo 2

- **Tipo 1**: se instala directamente como software de base. Comúnmente se utiliza en servidores.

- **Tipo 2**: se instala sobre el sistema operativo de la máquina.

### Anfitrión y sistemas invitados

El sistema operativo donde se ejecuta la máquina virtual es conocido como **anfitrión o host**. En cambio, el sistema operativo que se ejecuta dentro de una máquina virtual, es conocido como **sistema invitado o guest**.

## Vagrant

**Vagrant** es un software que nos permite **automatizar la instalación de máquinas virtuales**, además de darnos la posibilidad de instalar software o dependencias a través de un archivo de configuración. Esto nos permite **replicar fácilmente entornos de desarrollo iguales** en distintas máquinas fisicas.