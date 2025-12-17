import random # Importamos la librería para que la PC pueda elegir su jugada al azar.

# --- SECCIÓN DE FUNCIONES (Definimos nuestras herramientas personalizadas) ---

# Función para convertir el número que escribe el usuario a una palabra real.
def convertir_opcion(numero): # Usamos 'def' para crear la función llamada 'convertir_opcion'.
    # Creamos una LISTA con las palabras en el orden correcto.
    # El índice 0 es Piedra, el 1 es Papel y el 2 es Tijera.
    opciones = ["Piedra", "Papel", "Tijera"] 
    
    # Transformamos el texto que ingresó el usuario a un número entero.
    n = int(numero) 
    
    # Buscamos en la LISTA la palabra usando el número (restamos 1 porque Python cuenta desde 0).
    palabra = opciones[n - 1] 
    return palabra # Devolvemos la palabra encontrada al lugar donde se llamó la función.

# Función para determinar quién es el ganador comparando ambas jugadas.
def quien_gana(jugador, pc): # Usamos 'def' para crear la función 'quien_gana'.
    # Usamos una LISTA que guarda varias TUPLAS para definir las reglas de victoria.
    # Cada TUPLA representa: (Elemento que Gana, Elemento que Pierde).
    reglas = [
        ("Piedra", "Tijera"), # Tupla: Piedra vence a Tijera.
        ("Papel", "Piedra"),  # Tupla: Papel vence a Piedra.
        ("Tijera", "Papel")   # Tupla: Tijera vence a Papel.
    ]
    
    # Si ambas palabras son exactamente iguales, devolvemos un empate.
    if jugador == pc:
        return "empate" 
    
    # Creamos una TUPLA que junta la jugada del usuario y de la PC: (Usuario, PC).
    duelo_actual = (jugador, pc) 
    
    # Comprobamos si la TUPLA 'duelo_actual' existe dentro de nuestra LISTA de 'reglas'.
    if duelo_actual in reglas:
        return "usuario" # Si la combinación está en las reglas, el usuario gana.
    else:
        return "computadora" # Si no es empate ni ganó el usuario, gana la computadora.

# --- CUERPO PRINCIPAL DEL PROGRAMA (Donde corre el juego) ---

jugar = True # Variable booleana para mantener el ciclo encendido.

print("¡Hola! Bienvenido al juego de Piedra, Papel o Tijera.") # Mensaje de bienvenida.

while jugar == True: # Mientras la variable sea verdadera, el juego se repetirá.
    print("---------------------------------------") # Línea divisoria visual.
    print("1. Piedra | 2. Papel | 3. Tijera | 4. Salir") # Mostramos las opciones del menú.
    
    eleccion = input("Escribe el número de tu jugada: ") # Pedimos al usuario su elección.
    
    # Revisamos primero si el usuario decidió cerrar el programa.
    if eleccion == "4":
        print("Gracias por jugar, ¡adiós!") # Mensaje de despedida.
        jugar = False # Apagamos el ciclo cambiando la variable a Falsa.
        
    # Validamos que el número ingresado sea 1, 2 o 3 para evitar errores.
    elif eleccion in ["1", "2", "3"]:
        
        # Llamamos a nuestra FUNCIÓN para traducir el número a una palabra (Piedra, Papel o Tijera).
        usuario = convertir_opcion(eleccion) 
        
        # Creamos una LISTA de opciones para que la computadora elija una.
        lista_pc = ["Piedra", "Papel", "Tijera"] 
        computadora = random.choice(lista_pc) # La PC elige un elemento al azar de la LISTA.
        
        print(f"Tú: {usuario} vs PC: {computadora}") # Mostramos qué eligió cada uno.
        
        # Llamamos a la FUNCIÓN 'quien_gana' para procesar el resultado usando TUPLAS.
        resultado = quien_gana(usuario, computadora) 
        
        # Estructura condicional para mostrar el mensaje según el resultado obtenido.
        if resultado == "usuario":
            print("¡Ganaste esta ronda! 🎉") # Mensaje de victoria.
        elif resultado == "computadora":
            print("La computadora te ganó 😞") # Mensaje de derrota.
        else:
            print("¡Es un empate! 🤝") # Mensaje de empate.
            
    else:
        # Si el usuario ingresa cualquier otra cosa que no sea 1, 2, 3 o 4.
        print("Opción no válida, intenta de nuevo por favor")