# Programación orientada a objetos

Los conceptos son **transversales**(1) a través de los lenguajes de programación
orientados a objetos.

A las **clases** le podemos otorgar **atributos y métodos**, conocidos como **elementos 
o miembros** de clase (miembros estáticos).

A estos **miembros** le podemos otorgar un *scope* o alcance, que define en qué parte
del código podemos acceder a estos miembros.

1. Transversal: que cruza de un punto a otro.

## Objetos y paquetes

Una clase es un **modelo o abstracción** de un elemento del mundo real, y un **objeto** es una instancia de ese elemento, que puede tener otros valores para sus atributos y/o métodos.

Por ejemplo, la **clase Casa**, tendría atributos como: techo, puerta, ventanas.

Y un objeto de esa clase llamada **casaUno** puede tener 4 ventanas. El objeto llamado **casaDos** puede tener 2 ventanas.

Podemos crear un objeto a través del **constructor**. Por ejemplo: `Scanner lector = new Scanner(System.in);`. El constructor es el nombre de la clase, en este caso `Scanner`. Está implicito en el código por defecto. La **instancia o identificador** es el nombre que le queramos poner al objeto, en este caso `lector`.

El **constructor** va a generar el espacio suficiente en memoria para guardar nuestros objetos, con sus atributos y métodos no estáticos.

Notar que el constructor le da valores iniciales a los atributos y métodos, por defecto: **cero, false o null** dependiendo del tipo.

La palabra reservada **this**, referencia dentro de la clase al objeto que está accediendo desde fuera de la clase.

La **asignación en memoria** de los objetos y clases es manejada por **Java**. Y cada **objeto** es independiente el uno del otro.