from tareas import (
    agregar_tarea,
    mostrar_tareas,
    eliminar_tarea,
    editar_tarea,
    completar_tarea,
    buscar_tareas,
    filtrar_por_estado,
    guardar_tareas,
    cargar_tareas,
)

cargar_tareas()

def mostrar_menu() -> None:
    print("Seleccione una opción")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Eliminar tarea")
    print("4. Editar tarea")
    print("5. Completar tarea")
    print("6. Buscar tarea")
    print("7. Filtrar por estado")
    print("8. Salir")


def main() -> None:
    menu = {
        1: agregar_tarea,
        2: mostrar_tareas,
        3: eliminar_tarea,
        4: editar_tarea,
        5: completar_tarea,
        6: buscar_tareas,
        7: filtrar_por_estado,
    }

    while True:
        mostrar_menu()
        opcion = input("Opción: ").strip()

        if not opcion.isdigit():
            print("Ingresa un número válido.\n")
            continue

        opcion_num = int(opcion)

        if opcion_num == 8:
            print("Saliendo del programa...")
            break

        accion = menu.get(opcion_num)
        if accion:
            accion()
        else:
            print("Opción inválida.\n")


if __name__ == "__main__":
    main()
