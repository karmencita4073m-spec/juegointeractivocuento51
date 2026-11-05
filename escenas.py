from src.herramientas import (
    AMARILLOCLARO,
    AZULCLARO,
    MORADO,
    NEGRITA,
    RESET,
    elegir_opcion,
    esperar_continuar,
    imprimir_limpio,
    separador,
)


def escena_inicio():
    separador()
    imprimir_limpio("🏰 PARTE 1: El príncipe que no quería casarse")
    separador()
    imprimir_limpio("En un lejano reino de dragones y magia, vive el príncipe Eduard, heredero al trono. Es el más apuesto de los reinos cercanos, su melena rizada y sus ojos azules le han convertido en el más deseado también.")
    imprimir_limpio("Las princesas de los países vecinos lo desean, pero Eduard no se ha decidido por ninguna. Al contrario, se siente asediado y presionado.")
    imprimir_limpio(MORADO + NEGRITA + f"—Ninguna de esas princesas será ni mi esposa, ni mi futura reina. Prefiero quedarme solo —le dice a su padre, el rey." + RESET)
    imprimir_limpio("El rey se preocupa. Si su hijo no se casa y tiene hijos, ¿quién heredará el trono? Pero nadie puede obligar a Eduard contra su voluntad.")
    print("\n¿Qué piensas de la decisión de Eduard?")
    elegir_opcion([
        "Tiene razón —nadie debería obligarle a casarse",
        "Debería pensar en su reino y aceptar",
        "Espera a ver qué hace el mago..."
    ])
    esperar_continuar()

def escena_mago():
    separador()
    imprimir_limpio("🔮 PARTE 2: La imagen en el espejo")
    separador()
    imprimir_limpio("Eduard acude al mago de la corte,el unico con quien puede hablar con sinceridad de sus sentimientos)")
    imprimir_limpio("—Tal vez la mujer que buscas no esté en los confines de tu mundo —le dice el mago, acercándose a una fuente—. Mira.")
    imprimir_limpio("Con un movimiento de su mano, aparecen imágenes de lugares lejanos. Ciudades que brillan de noche, gente con ropas extrañas... Y entonces la ve.")
    imprimir_limpio("Una joven llamada Alicia. Vive en otra época, en otro mundo muy distinto al suyo. Y sin saber por qué, Eduard siente que la conoce de siempre.")
    print(AZULCLARO+ f"\n¿Qué decide hacer Eduard?")
    eleccion = elegir_opcion([
        "—Debo conocerla. Ayúdame a llegar hasta ella",
        "—Es imposible. No puedo ir a un lugar que no conozco",
        "—¿Y si no es ella quien creo?"
    ])
    if eleccion == 1:
        imprimir_limpio(MORADO + NEGRITA + "—Estoy dispuesto a todo —asegura Eduard—. Solo quiero tener la posibilidad de conocerla." + RESET)
    elif eleccion == 2:
        imprimir_limpio("—El amor no conoce fronteras —le recuerda el mago—. ¿No dijiste que preferías estar solo antes que elegir a la equivocada?")
    else:
        imprimir_limpio("—Solo hay una forma de averiguarlo —responde el mago—. Ve y descúbrelo tú mismo.")
    esperar_continuar()

def escena_viaje():
    separador()
    imprimir_limpio("🗽 PARTE 3: Bienvenido a Nueva York")
    separador()
    imprimir_limpio("El mago pronuncia unas palabras y todo cambia. El castillo desaparece. El aire frío de invierno le golpea.")
    imprimir_limpio("Se encuentra en una ciudad inmensa, llena de luces, ruidos y gente que viste de formas que jamás había imaginado.")
    imprimir_limpio(MORADO + NEGRITA + "—Parece que voy disfrazado a una fiesta —murmura Eduard mientras camina confundido entre la multitud." + RESET)
    imprimir_limpio("Llega a Central Park y ve un árbol enorme brillando con luces de colores. Se siente extraño, pero acogedor.")
    imprimir_limpio("Entonces ve un cartel en una farola. Con el rostro de Alicia anunciando su actuación esa misma noche.")
    imprimir_limpio(MORADO + NEGRITA + "—Te encontré —sonríe—. Al fin sé dónde estás.")
    esperar_continuar()

def escena_encuentro():
    separador()
    imprimir_limpio("💃 PARTE 4: Los ojos que se encontraron")
    separador()
    imprimir_limpio("Consigue llegar justo a tiempo. Le miran raro por sus ropas, pero no le importa. Solo tiene ojos para el escenario.")
    imprimir_limpio("Alicia aparece. Y cuando sus miradas se cruzan, algo sucede. El mundo parece detenerse.")
    imprimir_limpio("Ella no sabe quién es ese joven de ropas antiguas y mirada sincera. Pero siente que lo conoce de siempre.")
    imprimir_limpio("Cuando termina, él sale esperando hablar... pero ella ya se ha marchado.")
    imprimir_limpio(MORADO + NEGRITA + "—Mañana volveré —se dice a sí mismo—. Pero primero necesito un lugar donde pasar la noche. Y hace mucho frío." + RESET)
    esperar_continuar()

def escena_defensa():
    separador()
    imprimir_limpio("🛡️ PARTE 5: Una noche de nieve")
    separador()
    imprimir_limpio("Caminando sin rumbo, escucha un grito. Es Alicia. Un hombre la está amenazando en un callejón oscuro.")
    imprimir_limpio("Sin dudarlo, Eduard interviene. No es fuerte como el agresor, pero no se echa atrás. Alicia logra defenderse y juntos escapan.")
    imprimir_limpio("Viéndole solo y temblando de frío, Alicia le pregunta:")
    imprimir_limpio(AMARILLOCLARO+ NEGRITA + f"—¿Por qué no te quedas en mi casa esta noche? No es un palacio, pero estará caliente." + RESET)
    imprimir_limpio("Allí, entre sopa caliente y conversaciones extrañas, empiezan a conocerse. Eduard le cuenta quién es. Ella no le cree del todo... pero siente que hay verdad en sus ojos.")
    esperar_continuar()

def escena_secreto():
    separador()
    imprimir_limpio("🕯️ PARTE 6: Dos príncipes")
    separador()
    imprimir_limpio("Pero el mago aparece de la nada.")
    imprimir_limpio(MORADO + NEGRITA + "—Tu padre te necesita. Está enfermo. Y hay algo que debes saber antes de que sea tarde." + RESET)
    imprimir_limpio("En el castillo, el rey le confiesa la verdad: no era hijo único. Tenía un hermano gemelo que todos creían perdido al nacer. Aún vive.")
    imprimir_limpio("—Búscalo, hijo mío. Antes de que me vaya, quiero veros a los dos juntos.")
    esperar_continuar()

def escena_hermano():
    separador()
    imprimir_limpio("🤝 PARTE 7: Como dos gotas de agua")
    separador()
    imprimir_limpio("La búsqueda lleva a Eduard a una aldea humilde. Allí lo ve.")
    imprimir_limpio("Es como mirarse en un espejo. El mismo rostro, los mismos ojos. Solo que este joven se llama Eric y lleva una vida sencilla.")
    imprimir_limpio("Juntos regresan al castillo justo a tiempo. El rey los ve juntos, sonríe por última vez, y en paz, se va a reunir con su esposa.")
    imprimir_limpio("Los dos hermanos conversan y llegan a una decisión:")
    imprimir_limpio(MORADO + NEGRITA + f"—Reinaremos juntos. Seis meses cada uno. Unimos lo mejor de los dos mundos." + RESET)
    esperar_continuar()

def escena_final():
    separador()
    imprimir_limpio("💍 PARTE 8: Hechizo de Navidad")
    separador()
    imprimir_limpio("Eric encuentra su propia felicidad. Y Eduard regresa por Alicia. Ella abre la puerta y no puede creer que haya vuelto.")
    imprimir_limpio(MORADO + NEGRITA + f"—¿Te casarías conmigo mañana mismo, en mi reino?" + RESET)
    imprimir_limpio(AMARILLOCLARO + NEGRITA + "—Es una locura —sonríe ella con lágrimas en los ojos—. Pero sí. Me voy contigo." + RESET)
    imprimir_limpio("Se casaron el mismo día. Dos reyes, dos reinas, dos mundos que se unieron.")
    imprimir_limpio("Y el mago les regaló un portal entre los dos mundos. Cada Navidad regresan al lugar donde se conocieron. Porque el amor verdadero no conoce fronteras.")
    separador()
    print("✨" * 30)
    print("   F I N ✨ ¡Feliz Navidad! 🎄")
    print("   Gracias por jugar. Tu historia ha cobrado vida.")
    print("✨" * 30)
    separador()
