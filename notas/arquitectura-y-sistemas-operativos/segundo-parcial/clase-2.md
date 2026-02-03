# Ansible

Es una herramienta que permite **automatizar tareas**, como configuraciones de un equipo, instalar sofwtare y despliegue de aplicaciones.

Si tenemos muchos servidores, con Ansible podemos **configurarlos todos** de la misma manera.

### ¿Qué podemos automatizar?

- **Copias de seguridad**
- **Actualizaciones de software**
- **Reinicio de servicios**
- **Monitoreo del sistema**
- **Despliegue de servicios**

### ¿Cómo funciona Ansible?

Ansible se conecta a cada equipo a través de SSH a través de **dos archivos**.

Un archivo va a contener toda la lista de tareas a realizar (Playbook)

Y otro archivo que va a contener la lista de los equipos a los que se tiene que conectar, a través de su ip (Host Inventory).

### Idempotencia

Las tareas que se ejecutan en Ansible son **idempotentes**. Es decir, si vuelvo a ejecutar muchas veces la misma tarea que ya está resuelta simplemente no realiza ninguna acción.

#### Nota

Los equipos que vamos a configurar **no necesitan tener Ansible** instalados, solo la máquina desde la cual vamos a realizar los archivos de configuración.

### Playbooks

Cuando tenemos un proyecto grande, hay diferentes **roles** que ejecutan diferentes personas. Por ejemplo, unos se encargan de instalar los paquetes que necesita el equipo, otros de configurar aplicaciones, otros de las páginas web. Por eso con Ansible, podemos definir las **tareas** a través de **roles**, es decir, **cada persona o equipo escribe su propia tarea**.