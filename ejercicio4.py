inventario = {"cuadernos": 10, "lapices": 20, "borradores": 8}


# Acepta únicamente cantidades enteras mayores que cero.
def cantidad_valida(cantidad):
    return isinstance(cantidad, int) and not isinstance(cantidad, bool) and cantidad > 0


def consultar_stock(inv, producto):
    producto = producto.lower()
    return inv.get(producto, 0)


def agregar_stock(inv, producto, cantidad):
    producto = producto.lower()
    if cantidad_valida(cantidad):
        inv[producto] = inv.get(producto, 0) + cantidad
        print(
            f"Se agregaron {cantidad} unidades de '{producto}'. Stock actual: {inv[producto]}"
        )
        return True
    else:
        print("La cantidad a agregar debe ser un entero positivo.")
        return False


def vender_producto(inv, producto, cantidad):
    producto = producto.lower()
    if not cantidad_valida(cantidad):
        print("La cantidad a vender debe ser un entero positivo.")
        return False

    stock_actual = inv.get(producto, 0)
    if producto not in inv:
        print(f"El producto '{producto}' no existe en el inventario.")
        return False

    if cantidad > stock_actual:
        print(
            f"Rechazado: Stock insuficiente para '{producto}'. Disponibles: {stock_actual}, Solicitados: {cantidad}"
        )
        return False

    inv[producto] -= cantidad
    print(
        f"Venta exitosa: {cantidad} unidades de '{producto}'. Quedan: {inv[producto]}"
    )
    return True


if __name__ == "__main__":
    print("--- PRUEBAS DE INVENTARIO ---")
    print("Inventario inicial:", inventario)
    vender_producto(inventario, "cuadernos", 3)
    vender_producto(inventario, "cuadernos", 15)
    agregar_stock(inventario, "marcadores", 4)
    agregar_stock(inventario, "lapices", 1.5)