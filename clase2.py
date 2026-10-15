import math

def calcular_area_circulo(radio):
    if radio < 0:
        return None
    # El área corresponde a pi multiplicado por el radio al cuadrado.
    return math.pi * radio**2


if __name__ == "__main__":
    print("\n--- Ejercicio 2: Área de un Círculo ---")
    try:
        radio = float(input("Ingrese el radio del círculo: "))
        area = calcular_area_circulo(radio)
        if area is None:
            print("Error: El radio no puede ser negativo.")
        else:
            print(f"El área del círculo con radio {radio} es: {area:.2f}")
    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")