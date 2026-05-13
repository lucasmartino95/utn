# Abstracción

Las **clases abstractas** son aquellas entidades que no se pueden tocar, 
como **Animal o Vehículo**.

Para definir un método abstracto dentro 
de una de estas clases, usamos: `public abstract void acelerar();`.

Luego la **clase hija** deberá implementar el método `acelerar` obligatoriamente 
**sobrescribiendo** el método abstracto de su clase padre.

Las **clases abstractas** pueden tener los mismos elementos que las clases comúnes y además, **métodos abstractos**.

La **única clase que está obligada** a sobrescribir un método abstracto, es la primer clase derivada.