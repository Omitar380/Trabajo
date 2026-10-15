# Cada operación recibe dos números y devuelve su resultado.
def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return None
    return a / b


def calculadora():
    print("--- CALCULADORA BÁSICA ---")
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
        return

    print("Seleccione la operación (+, -, *, /):")
    operacion = input("Operación: ").strip()

    if operacion == "+":
        resultado = sumar(num1, num2)
    elif operacion == "-":
        resultado = restar(num1, num2)
    elif operacion == "*":
        resultado = multiplicar(num1, num2)
    elif operacion == "/":
        if num2 == 0:
            print("Error: No se puede dividir entre cero.")
            return
        resultado = dividir(num1, num2)
    else:
        print("Operación no válida.")
        return

    print(f"El resultado es: {resultado}")


if __name__ == "__main__":
    
    calculadora()