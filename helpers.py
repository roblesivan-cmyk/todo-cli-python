def leer_int(mensaje: str) -> int | None:
    """Lee un entero desde input. Regresa None si es inválido."""
    try:
        return int(input(mensaje))
    except ValueError:
        print("ID inválido. Debe ser un número.")
        return None


def leer_texto(mensaje: str, permitir_vacio: bool = False) -> str:
    """Lee texto, aplica strip(). Si no permite vacío, vuelve a pedir."""
    while True:
        txt = input(mensaje).strip()
        if permitir_vacio or txt:
            return txt
        print("El texto no puede ir vacío.")


def leer_estado(mensaje: str, permitir_vacio: bool = False) -> str | None:
    """
    Lee estado: pendiente/completada.
    Si permitir_vacio=True y el usuario deja vacío, regresa "".
    Si es inválido, regresa None.
    """
    estado = input(mensaje).strip().lower()

    if permitir_vacio and estado == "":
        return ""

    if estado in ("pendiente", "completada"):
        return estado

    print("Estado inválido. Usa 'pendiente' o 'completada'.")
    return None
