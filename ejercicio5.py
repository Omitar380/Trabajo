
asignaturas = ("Programación", "Matemáticas", "Inglés")


def calcular_promedio(notas):
    return sum(notas) / len(notas) if notas else 0.0


def registrar_estudiantes(asignaturas):
    estudiantes = []
    print("\n--- REGISTRO DE 3 ESTUDIANTES ---")
    # Cada estudiante debe registrar una nota válida por asignatura.
    for i in range(3):
        print(f"\nEstudiante #{i + 1}")
        nombre = input("Nombre del estudiante: ").strip()
        notas = []

        for asignatura in asignaturas:
            while True:
                try:
                    nota = float(
                        input(
                            f"  Nota en {asignatura} (0.0 a 5.0): "
                        )
                    )
                    if 0.0 <= nota <= 5.0:
                        notas.append(nota)
                        break
                    else:
                        print("    Error: La nota debe estar entre 0.0 y 5.0.")
                except ValueError:
                    print("    Error: Ingrese un valor numérico válido.")

        estudiante = {"nombre": nombre, "notas": notas}
        estudiantes.append(estudiante)

    return estudiantes


def mostrar_reporte(estudiantes, asignaturas):
    print("\n" + "=" * 50)
    print("                 REPORTE GENERAL                 ")
    print("=" * 50)

    mayor_promedio = -1
    ganadores_promedio = []

    for est in estudiantes:
        nombre = est["nombre"]
        notas = est["notas"]
        promedio = calcular_promedio(notas)
        estado = "Aprobado" if promedio >= 3.0 else "Reprobado"

        print(f"\nEstudiante: {nombre}")
        for i, asignatura in enumerate(asignaturas):
            print(f" - {asignatura}: {notas[i]}")
        print(f"Promedio: {promedio:.2f}")
        print(f"Estado: {estado}")

        if promedio > mayor_promedio:
            mayor_promedio = promedio
            ganadores_promedio = [nombre]
        elif promedio == mayor_promedio:
            ganadores_promedio.append(nombre)

    print("\n" + "-" * 50)
    if len(ganadores_promedio) == 1:
        print(
            f"🏆 Estudiante con el promedio más alto: {ganadores_promedio[0]} ({mayor_promedio:.2f})"
        )
    elif len(ganadores_promedio) > 1:
        print(
            f"🏆 Empate en el promedio más alto ({mayor_promedio:.2f}) entre: {', '.join(ganadores_promedio)}"
        )
    print("=" * 50)

if __name__ == "__main__":
    estudiantes_registrados = registrar_estudiantes(asignaturas)
    mostrar_reporte(estudiantes_registrados, asignaturas)