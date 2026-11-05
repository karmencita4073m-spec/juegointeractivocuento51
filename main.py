from src.escenas import (
    escena_defensa,
    escena_encuentro,
    escena_final,
    escena_hermano,
    escena_inicio,
    escena_mago,
    escena_secreto,
    escena_viaje,
)


def jugar() -> None:
    print("🎄" * 25)
    print("   H E C H I Z O   E N   N A V I D A D")
    print("   Versión desarrollo modular")
    print("🎄" * 25)
    input("\nPulsa ENTER para empezar...")

    escena_inicio()
    escena_mago()
    escena_viaje()
    escena_encuentro()
    escena_defensa()
    escena_secreto()
    escena_hermano()
    escena_final()


if __name__ == "__main__":
    jugar()
