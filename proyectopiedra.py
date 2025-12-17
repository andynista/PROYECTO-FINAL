import random # Importa el módulo 'random', necesario para que la computadora elija su jugada.

# -------------------------------------------------------------
# 1. Funciones de Mapeo y Lógica
# -------------------------------------------------------------

def obtener_eleccion_mapeada(opcion_num):
    """
    Traduce la entrada numérica del usuario a la jugada de texto (Piedra, Papel o Tijera)
    utilizando un diccionario para un mapeo eficiente (en lugar de if/elif anidados).
    """
    # Diccionario para mapear la entrada (string) a la jugada (string).
    mapeo = {
        "1": "Piedra",
        "2": "Papel",
        "3": "Tijera"
    }
    # .get() es seguro: si la opción no existe, devuelve None.
    return mapeo.get(opcion_num)

def determinar_ganador(usuario, computadora):
    """
    Contiene la lógica central del juego para determinar el resultado de la ronda.
    Recibe las jugadas en formato de texto (string).
    """
    # Lista (list) de tuplas para definir las reglas de victoria: (Ganador, Perdedor)
    reglas_victoria = [
        ("Piedra", "Tijera"), # La Piedra gana a la Tijera
        ("Papel", "Piedra"),  # El Papel gana a la Piedra
        ("Tijera", "Papel")   # La Tijera gana al Papel
    ]

    if usuario == computadora:
        return "empate" # Retorna "empate" si ambas jugadas son iguales.
    
    # Comprueba si la tupla de la jugada del usuario está en la lista de reglas_victoria.
    elif (usuario, computadora) in reglas_victoria:
        return "usuario" # Retorna "usuario" si la combinación cumple una regla de victoria.
        
    else:
        return "computadora" # Si no es empate ni victoria del usuario, gana la computadora.

# -------------------------------------------------------------
# 2. Función Principal del Juego
# -------------------------------------------------------------

def jugar_ronda():
    """
    Ejecuta una sola ronda del juego: solicita la entrada, calcula la jugada de la computadora 
    y anuncia el resultado.
    """
    print("............................................")
    print("--- MENÚ ---")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("4. Salir")
    print("............................................")

    # Solicita la elección del usuario (se recibe como string).
    opcion_usuario = input("Ingresa tu elección (1-4): ")

    if opcion_usuario == "4":
        return False, "Gracias por jugar. ¡SALIENDO DEL JUEGO! 👋" # Retorna False para detener el bucle
    
    eleccion_usuario = obtener_eleccion_mapeada(opcion_usuario) # Llama a la función de mapeo.
    
    if eleccion_usuario is None:
        return True, "❌ Opción no VALIDA. Por favor, ingresa un número válido (1, 2, 3 o 4)." # Retorna True para seguir jugando
    
    # Define la lista de opciones disponibles para la computadora.
    opciones_juego = ["Piedra", "Papel", "Tijera"] 
    # La computadora elige un elemento al azar de la lista.
    eleccion_computadora = random.choice(opciones_juego) 
    
    # Muestra las jugadas
    print(f"Tú elegiste: **{eleccion_usuario}**")
    print(f"La computadora eligió: **{eleccion_computadora}**")
    
    # Llama a la función de lógica para determinar el ganador.
    ganador = determinar_ganador(eleccion_usuario, eleccion_computadora) 
    
    # Anuncia el resultado
    if ganador == "usuario":
        resultado_msg = "🎉 ¡GANO EL JUEGO!"
    elif ganador == "computadora":
        resultado_msg = "😞 La computadora ganó ESTE JUEGO"
    else:
        resultado_msg = "🤝 ¡ES UN EMPATE!"
        
    return True, resultado_msg # Retorna True para continuar y el mensaje de resultado.

# -------------------------------------------------------------
# 3. Punto de Entrada del Programa (Main Loop)
# -------------------------------------------------------------

print("👋 ¡Bienvenido al juego de Piedra, Papel o Tijera!")

jugar = True # Inicializa la variable de control booleana.
while jugar: # Bucle principal que se ejecuta mientras 'jugar' sea True.
    # Llama a la función que ejecuta la ronda y obtiene el estado de continuación y el mensaje.
    jugar, mensaje_ronda = jugar_ronda() 
    print(mensaje_ronda) # Imprime el mensaje (resultado o error/salida).