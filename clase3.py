def calcular_precio_venta(costo_produccion):
    if costo_produccion < 0:
        return None

    # Utilidad e impuestos se calculan sobre el costo de producción.
    utilidad = costo_produccion * 1.20
    impuestos = costo_produccion * 0.15
    precio_venta = costo_produccion + utilidad + impuestos
    return utilidad, impuestos, precio_venta


if __name__ == "__main__":
    print("\n--- Ejercicio 3: Precio de Venta de un Artículo ---")
    nombre_producto = input("Ingrese el nombre del producto: ")

    try:
        costo_produccion = float(input("Ingrese el costo de producción: "))
        resultado = calcular_precio_venta(costo_produccion)
        if resultado is None:
            print("Error: El costo de producción no puede ser negativo.")
        else:
            utilidad, impuestos, precio_venta = resultado
            print("\n--- DETALLE DE VENTA ---")
            print(f"Producto: {nombre_producto}")
            print(f"Costo de producción: ${costo_produccion:,.2f}")
            print(f"Utilidad (120%): ${utilidad:,.2f}")
            print(f"Impuestos (15%): ${impuestos:,.2f}")
            print(f"Precio de venta final: ${precio_venta:,.2f}")
    except ValueError:
        print("Por favor, ingrese un valor numérico válido para el costo.")