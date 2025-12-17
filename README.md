# PROYECTO-FINAL
PROYECTO INTEGRADOR PAR AEL JUEGO PIEDRA, PAPEL O TIJERA MEDIANTE EL USO DE FUNCIONES
Juego: Piedra, Papel o Tijera (Versión Modular)
Descripción:
Este programa es una versión mejorada del clásico juego "Piedra, Papel o Tijera". A diferencia de las versiones lineales básicas, este código utiliza Programación Modular, lo que significa que el juego se divide en funciones específicas para procesar datos y determinar resultados.
Este programa permite al usuario jugar contra la computadora de forma infinita hasta que decida salir voluntariamente.
Objetivos del Proyecto:
Aplicar Funciones (def): Segmentar el código en tareas lógicas (traducción de datos y reglas de juego).
Gestión de Datos con Listas: Utilizando estructuras de listas para almacenar opciones y facilitar el acceso mediante índices.
Uso de Tuplas: Implementar tuplas para representar reglas fijas e inmutables de victoria.
Interactividad: Crear un menú robusto que valide las entradas del usuario.
Conversión de Datos: Transforma la entrada numérica del usuario (1, 2, 3) en texto descriptivo usando una lista de referencia.

Lógica de Reglas Fijas: Utiliza una Lista de Tuplas para verificar quién gana, eliminando la necesidad de múltiples condicionales if/and/or complejos.

Oponente Aleatorio: Implementa el módulo random para que la computadora elija una jugada impredecible de una lista de opciones.

Validación de Errores: Incluye un filtro para entradas no válidas, evitando que el programa se cierre por errores de escritura.
Estructura:
convertir_opcion(),Función,Traduce el número del menú a la palabra correspondiente.
quien_gana(),Función,Procesa el resultado de la ronda comparando las elecciones.
opciones,Lista,"Almacena las jugadas disponibles: Piedra, Papel, Tijera."
reglas,Lista de Tuplas,"Contiene los "pares de victoria"" (ej. Piedra vence a Tijera)."
duelo_actual,Tupla,Empaqueta las jugadas de la ronda para una comparación rápida.

Cómo ejecutarlo
Asegúrate de tener Python 3.x instalado en tu computadora.

Descarga el archivo del código (proyectopiedra.py).

Abre una terminal o consola y ejecuta:
Información del Desarrollador: Carlos Andres Chango estudiante UIDE
Lenguaje: Python

Fecha de creación: 16 de diciembre de 2025

Enfoque: Académico / Estudiante de Programación

