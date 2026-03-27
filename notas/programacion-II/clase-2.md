# Fundamentos de POO

Encapsulamiento: tiene que ver con el alcance que tienen nuestras clases y objetos
dentro del código.

Abstracción: pasar a código los atributos y comportamientos que tiene un objeto de 
la vida real.

Herencia:

Polimorfismo:

## Principio DRY

Este principio tiene que ver con la calidad del código, **Don't repeat yourself** define
que si ya resolvimos un problema, no volver a resolverlo dentro del código, sino reutilizar
lo que ya hicimos.

## Miembros estáticos y no estáticos

**Miembro estático**:

- Lleva la palabra reservada `static`
- Se pueden llamar: miembro estático o miembro de clase
- Se invoca así: Clase.Miembro

Si lo llamamos desde una clase ya sabemos que el miembro es estático (ya sea un atributo o un método).

**Miembro no estático**:

- NO Lleva la palabra reservada `static`
- Se pueden llamar: miembro de instancia o miembro no estático
- Se invoca así: objeto.Metodo

Si lo llamamos desde un objeto que creamos, ya sabemos que el miembro 
es no estático (ya sea un atributo o un método).