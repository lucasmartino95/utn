# Vagrant

Para crear una máquina virtual, se debe ir a la carpeta donde está el Vagrantfile, y correr el siguiente comando: 

`vagrant up`

Luego que la máquina está creada y prendida, para conectarnos, usamos:

`vagrant ssh`

Para salir de la máquina virtual y apagarla, primero escribimos: `exit` en la consola dentro de la máquina virtual, y una vez que estamos fuera: `vagrant halt`

# SSH

**SSH** es un protocolo de red que permite establecer conexiones seguras, cifradas, entre ordenadores.

Para conectarnos a GitHub, podemos utilizar SSH, y así no será necesario ingresar la contraseña de nuestra cuenta cada vez que queramos realizar una acción en GitHub desde nuestro repositorio local.

[Guía para conectarse a GitHub a través de SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

Notar que al generar una clave nos creará una clave pública y una privada. La clave pública es la que podemos compartir. 