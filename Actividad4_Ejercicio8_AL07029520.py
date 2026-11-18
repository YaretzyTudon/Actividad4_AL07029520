
print("ACTIVIDAD 4 - EJERCICIO 8")
print("Nombre: Yaretzy Tudon Escamilla")
print("Matrícula: AL07029520")
print("Tablero del almacén refrigerado")

# Constantes de los equipos
REFRIGERACION = 1
LUCES = 2
ALARMA = 4
BANDA = 8

# Pedir información
estado = int(input("Estado actual (0-15): "))
cambio = int(input("Equipo a cambiar (1, 2, 4 u 8): "))

# Validar los datos
if not (0 <= estado <= 15):
    print("Estado no válido")

elif not (cambio == 1 or cambio == 2 or cambio == 4 or cambio == 8):
    print("Código de equipo no válido")

else:
    # Cambiar el estado del equipo
    nuevo = estado ^ cambio

    # Identificar equipos apagados
    apagados = ~nuevo & 15

    print("Nuevo estado:", format(nuevo, "04b"), nuevo)
    print("Equipos apagados:", format(apagados, "04b"))

    nombres = []

    if apagados & REFRIGERACION:
        nombres.append("Refrigeración")
    if apagados & LUCES:
        nombres.append("Luces")
    if apagados & ALARMA:
        nombres.append("Alarma")
    if apagados & BANDA:
        nombres.append("Banda transportadora")

    print("Apagados:", ", ".join(nombres))

    if nuevo & REFRIGERACION == 0:
        print("ALERTA: Refrigeración apagada")
