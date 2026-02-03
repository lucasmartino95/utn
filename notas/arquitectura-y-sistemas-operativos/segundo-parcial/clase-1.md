# ¿Qué es una partición?

Es un **espacio propio** para definir distintas cosas. Significa **dividir un disco físico en varios discos lógicos**. Esta división permite una mejor organización y gestión del espacio de almacenamiento.

Si se rompe alguna de las particiones no afecta a las otras particiones, por ejemplo la del sistema operativo.

Podemos tener hasta 4 particiones de **tipo primario**. Si queremos tener por ejemplo, 5 particiones, debemos crear **particiones lógicas** dentro de una partición extendida.

En los primeros sectores del disco duro se almacena la **tabla de particiones** y los archivos de **booteo**.

Para **Windows** cada partición es un disco diferente.

En **Linux** cada disco y sus particiones se encuentran dentro del directorio **/dev**. Nombra al disco como **sda** y la partición como **sda1**. Además cada partición la ve como un archivo.

Todos los discos deben tener **al menos una partición**. Cada partición debe estar formateada de acuerdo al sistema de archivos que utilizemos. En **Linux** por ejemplo el sistema de archivos más utilizado es **ext4**.

## Tipos de almacenamiento

#### A través de la red

Es el almacenamiento que utilizamos a través de internet. Por ejemplo cuando guardamos cosas en un servidor.

#### RAID

La **tecnología RAID** se utiliza para mejorar el rendimiento del equipo, también para brindar mayor seguridad al almacenamiento de datos. Utiliza siempre más de un disco. Almacena los archivos en dos discos físicos a la vez.

- **RAID 0**: Utiliza dos discos para almacenar archivos. Por ejemplo almacena la mitad de un archivo en un disco y la otra mitad en el otro.

- **RAID 1**: Utiliza dos discos utilizando un espejo. Es decir almacena el mismo archivo en dos discos a la vez.

- **RAID 5**: Es una combinación de RAID 0 y RAID 1. Se necesitan tres discos.

Se puede **implementar** a través del hardware o del software.

### LVM

Agrupa todos los discos en volúmenes lógicos. Lo que permite esta tecnología es **redimensionar el espacio** de manera dinámica de cada volumen lógico. **También permite migrar datos**.

#### Componentes principales de LVM

- **Physical Volume (PV)**:  Discos o particiones físicas donde LVM asigna el almacenamiento.

- **Volume Group (VG)**: Grupo que contiene varios PVs, combinandolos en una única unidad de almacenamiento. 

- **Logical Volume (LV)**: Las "particiones" que los usuarios y sistemas ven como discos, creadas a partir de los VGs.