import math

def calcular_raiz_cuarta(numero):
    # La raíz cuarta equivale a calcular dos raíces cuadradas.
    if numero < 0:
        return None
    return math.sqrt(math.sqrt(numero))


if __name__ == "__main__":
    print("--- Ejercicio 1: Raíz Cuarta ---")
    try:
        numero = float(input("Ingrese un número real: "))
        resultado = calcular_raiz_cuarta(numero)
        if resultado is None:
            print("Error: No se puede calcular la raíz de un número negativo.")
        else:
            print(f"La raíz cuarta de {numero} es: {resultado}")
    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")