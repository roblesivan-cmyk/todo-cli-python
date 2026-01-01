from helpers import leer_int, leer_texto, leer_estado
import json 
import os

ARCHIVO = "tareas.json"


def cargar_tareas() -> None:
    global tareas
    
    if not os.path.exists(ARCHIVO):
        tareas = []
        return
    with open(ARCHIVO, "r", encoding = "utf-8") as f:
        tareas = json.load(f)

def guardar_tareas():
    with open(ARCHIVO, "w", encoding = "utf-8") as f:
        json.dump(tareas, f, indent=4, ensure_ascii=False)
# Lista principal de tareas (cada tarea es un dict)
tareas: list[dict] = []


def id_existe(task_id: int) -> bool:
    return any(t["id"] == task_id for t in tareas)


def agregar_tarea() -> None:
    task_id = leer_int("Ingrese ID: ")
    if task_id is None:
        return

    if id_existe(task_id):
        print("Ese ID ya existe. Usa otro.")
        return

    descripcion = leer_texto("Ingrese descripción: ")
    estado = leer_estado("Ingrese estado (pendiente/completada): ")
    if estado is None:
        return

    tarea = {"id": task_id, "descripcion": descripcion, "estado": estado}
    tareas.append(tarea)
    guardar_tareas()
    print("Tarea agregada con éxito.")


def mostrar_tareas() -> None:
    print("\nTareas actuales:")
    if not tareas:
        print("No hay tareas para mostrar.\n")
        return

    for t in tareas:
        print(f"[{t['id']}] {t['descripcion']} - {t['estado']}")
    print()


def eliminar_tarea() -> None:
    task_id = leer_int("Ingrese ID de la tarea a eliminar: ")
    if task_id is None:
        return

    antes = len(tareas)
    tareas[:] = [t for t in tareas if t["id"] != task_id]
    despues = len(tareas)

    if despues < antes:
        print("Tarea eliminada.")
        guardar_tareas()
    else:
        print("No se encontró una tarea con ese ID.")


def editar_tarea() -> None:
    task_id = leer_int("Ingrese ID de la tarea a modificar: ")
    if task_id is None:
        return

    for t in tareas:
        if t["id"] == task_id:
            nueva_desc = leer_texto("Nueva descripción (Enter para no cambiar): ", permitir_vacio=True)
            nuevo_estado = leer_estado("Nuevo estado (pendiente/completada, Enter para no cambiar): ", permitir_vacio=True)

            if nuevo_estado is None:  # inválido
                return

            if nueva_desc != "":
                t["descripcion"] = nueva_desc
                print("Descripción actualizada.")
            else:
                print("No se cambió la descripción.")

            if nuevo_estado != "":
                t["estado"] = nuevo_estado
                print("Estado actualizado.")
            else:
                print("No se cambió el estado.")

            print("Cambios realizados con éxito.")
            guardar_tareas()
            return

    print("No se encontró una tarea con ese ID.")


def completar_tarea() -> None:
    task_id = leer_int("Ingrese ID de la tarea a completar: ")
    if task_id is None:
        return

    for t in tareas:
        if t["id"] == task_id:
            if t["estado"] == "completada":
                print("Esa tarea ya está completada.")
            else:
                t["estado"] = "completada"
                print("Tarea marcada como completada.")
                guardar_tareas()
            return

    print("No se encontró una tarea con ese ID.")


def buscar_tareas() -> None:
    palabra = leer_texto("Buscar (palabra o frase): ", permitir_vacio=True).lower()
    if palabra == "":
        print("Búsqueda vacía.")
        return

    encontrados = [t for t in tareas if palabra in t["descripcion"].lower()]
    if encontrados:
        print("\nResultados:")
        for t in encontrados:
            print(f"[{t['id']}] {t['descripcion']} - {t['estado']}")
        print()
    else:
        print("No se encontraron tareas con ese texto.")


def filtrar_por_estado() -> None:
    estado = leer_estado("Filtrar por (pendiente/completada): ")
    if estado is None:
        return

    filtradas = [t for t in tareas if t["estado"] == estado]
    if filtradas:
        print()
        for t in filtradas:
            print(f"[{t['id']}] {t['descripcion']} - {t['estado']}")
        print()
    else:
        print(f"No hay tareas en estado '{estado}'.")
