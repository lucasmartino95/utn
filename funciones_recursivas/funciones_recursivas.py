from Input import *

numero_usuario = get_int("")


def sumar_naturales(numero: int) -> int:

    if numero == 0:
        return 0
    else:
        total = numero + sumar_naturales(numero - 1)
    return total


print(f"La suma de los números naturales hasta {numero_usuario} es: \
{sumar_naturales(numero_usuario)}")

print("-------")

print("Cacular la potencia de un número:")
base = get_int("BASE")
exponente = get_int("EXPONENTE")

def calcular_potencia(base: int, exponente: int) -> int:

    if exponente == 0:
        resultado = 1
    else:
        resultado = base * calcular_potencia(base, exponente - 1)
        
    return resultado


print(f"{base} elevado a {exponente} es: {calcular_potencia(base, exponente)}")

print("-------")

numero_digitos = get_int("Calcula los dígitos de un número: ")


def sumar_digitos(numero: int) -> int:

    if numero < 10:
        return numero
    else:
        ultimo_digito = numero % 10
        resto_numero = numero // 10
        return ultimo_digito + sumar_digitos(resto_numero)


print(sumar_digitos(numero_digitos))


numero_fibonacci = get_int("Calcula el número de Fibonacci de un número: ")


def calcular_fibonacci(numero: int) -> int:

    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    elif numero > 1:
        numero = calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)
        return numero
    

print(calcular_fibonacci(numero_fibonacci))