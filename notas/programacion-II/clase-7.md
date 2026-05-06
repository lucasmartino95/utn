# Herencia

Es la **relación entre una o más clases** en las que se comparten 
atributos y métodos definidos en otra clase. No hay límite de número 
para estas relaciones.

Por ejemplo, podemos tener la clase Animal, y luego las clases **derivadas/hijas/subclases**:
Perro y Gato.

La **clase base/super/padre** es una **generalización** de un grupo de características y comportamientos que tienen en común las clases derivadas. Mientras que las **clases derivadas** son una **especialización** de la clase base.

En **Java** todo deriva de la clase **Object** implícitamente.

## Tipos de herencia

- **Simple**: las clases derivadas solo pueden tener una clase padre.

- **Múltiple**: las clases derivadas pueden tener varias clases padre, lo cual no está permitido en **Java**.

Notar que la clase padre nunca conoce a sus hijos, por ejemplo la clase **Animal** no sabe si puede ser un **Perro** o un **Gato**. Por eso se dice que las clases hijo siempre miran hacia arriba, queriendo decir que un **Perro** o un **Gato** saben que son de la clase **Animal**.

## ¿Cómo se codifica?

```Java
public class Animal {
    private String nombre;
    private String tipoAlimentacion;
    private int edad;

    public void comer() {
        return true;
    }
    public void dormir() {
        return true;
    }
}

public class Perro extends Animal {
    private String raza;

    public void ladrar() {
        return true;
    }
}

public class Gato extends Animal {
    private String pedigri;

    public void maullar() {
        return true;
    }
}
```