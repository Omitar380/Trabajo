
# Cada producto se representa con una tupla (código, nombre, precio).
productos = [
    ("P01", "Teclado", 45000),
    ("P02", "Mouse", 25000),
    ("P03", "Memoria USB", 30000),
]


def mostrar_productos(lista_productos):
    print("\n--- CATÁLOGO DE PRODUCTOS ---")
    for codigo, nombre, precio in lista_productos:
        print(f"Código: {codigo} | Producto: {nombre} | Precio: ${precio:,}")


def buscar_producto(lista_productos, codigo_buscado):
    for codigo, nombre, precio in lista_productos:
        if codigo.upper() == codigo_buscado.upper():
            return nombre, precio
    return None


if __name__ == "__main__":
    mostrar_productos(productos)
    codigo_ingresado = input(
        "\nIngrese el código del producto a buscar: "
    )
    resultado = buscar_producto(productos, codigo_ingresado)

    if resultado:
        nombre, precio = resultado
        print(f"¡Producto encontrado! Nombre: {nombre}, Precio: ${precio:,}")
    else:
        print("El código ingresado no existe en el catálogo.")