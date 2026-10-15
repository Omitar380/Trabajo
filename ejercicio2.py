def calcular_promedio(notas):
    return sum(notas) / len(notas) if notas else 0.0


def obtener_mayor(notas):
    return max(notas) if notas else 0.0


def obtener_menor(notas):
    return min(notas) if notas else 0.0


def registrar_notas():
    notas = []
    print("\n--- REGISTRO DE 5 NOTAS (0.0 a 5.0) ---")
    # Solo se guardan notas que estén dentro del rango permitido.
    while len(notas) < 5:
        try:
            nota = float(
                input(
                    f"Ingrese la nota #{len(notas) + 1} (entre 0.0 y 5.0): "
                )
            )
            if 0.0 <= nota <= 5.0:
                notas.append(nota)
            else:
                print("Nota fuera de rango. Debe estar entre 0.0 y 5.0.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")

    promedio = calcular_promedio(notas)
    mayor = obtener_mayor(notas)
    menor = obtener_menor(notas)

    print(f"\nNotas registradas: {notas}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Nota más alta: {mayor}")
    print(f"Nota más baja: {menor}")

    if promedio >= 3.0:
        print("Estado: ¡APROBADO!")
    else:
        print("Estado: REPROBADO")


notas_prueba = [4.0, 3.5, 2.5, 5.0, 3.0]
print(
    f"Prueba con {notas_prueba} -> Promedio:", calcular_promedio(notas_prueba)
)

if __name__ == "__main__":
    registrar_notas()