import time


# Colores
PLATA = "\033[97m"
NEGRITA = "\033[1m"
RESET = "\033[0m"
MORADO = "\033[95m"
AZULCLARO = "\033[94m"
BLANCOBRIILLANTE = "\033[97m"
AMARILLOCLARO = "\033[93m"


def imprimir_limpio(texto: str) -> None:
    # Muestra texto con pausa para lectura
    print(texto)
    time.sleep(1.5)


def separador() -> None:
    # Línea separadora visual
    print(MORADO + "\n" + "-" * 60 + "\n" + RESET)


def esperar_continuar() -> None:
    # Pausa hasta pulsar Enter
    
    input(PLATA + "Pulsa Enter para continuar" + RESET)


def elegir_opcion(opciones: list[str]) -> int:
    # Muestra opciones y devuelve el número seleccionado
    if not opciones:
        raise ValueError("Debe haber al menos una opción.")

    for i, opcion in enumerate(opciones, start=1):
        print(f" {i}. {opcion}")

    while True:
        eleccion = input("\nTu elección: ").strip()
        if eleccion.isdecimal():
            numero = int(eleccion)
            if 1 <= numero <= len(opciones):
                return numero
        print(
            PLATA
            + f"Por favor, escribe un número del 1 al {len(opciones)}."
            + RESET
        )