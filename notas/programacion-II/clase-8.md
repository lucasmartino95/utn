# Polimorfismo

Es un concepto transversal a todos los lenguajes de programación.
**Poli** es mucho y **morfo** formas. Hay varios tipos:

- **Ad hoc**: en Java, sobrecarga de métodos y en otros lenguajes también de operadores. Acceder a un **método que cambie de forma** dependiendo de los parámetros que le pase o no al método.

- **Ad hoc por coerción**: es cuando un tipo de dato cambia a otro.

- **Polimorfismo universal**:
    - **Paramétrico**: ocurre cuando un método o una clase es genérica y puede trabajar con cualquier tipo de datos.
    - **Por inclusión**: se basa en herencia y sobreescritura (no es lo mismo que sobrecargar) de métodos. 
        - sobreescritura es cambiar el comportamiento de un método con la misma firma, es decir, **mismos modificadores de acceso, retorno y parámetros**.

Las **maneras más comunes** de usar polimorfismo pueden ser sobreescribir `toString();` o `equals();`.