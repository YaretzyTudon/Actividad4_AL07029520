
print("ACTIVIDAD 4 - EJERCICIO 6")
print("Nombre: Yaretzy Tudon Escamilla")
print("Matrícula: AL07029520")
print("Servicios de dos navieras")

# Constantes de los servicios
FLETE = 1
SEGURO = 2
DESPACHO = 4
ALMACENAJE = 8

# Pedir los códigos de las dos navieras
naviera1 = int(input("Código de servicios de naviera 1 (0-15): "))
naviera2 = int(input("Código de servicios de naviera 2 (0-15): "))

# Validar los códigos
if not (0 <= naviera1 <= 15 and 0 <= naviera2 <= 15):
    print("Código no válido")
else:
    # Operaciones bit a bit
    en_comun = naviera1 & naviera2
    alguno = naviera1 | naviera2
    solo_una = naviera1 ^ naviera2

    # Mostrar resultados
    print("Servicios en común:", format(en_comun, "04b"), en_comun)
    print("Servicios de al menos una:", format(alguno, "04b"), alguno)
    print("Servicios de solo una:", format(solo_una, "04b"), solo_una)

    # Identificar los servicios en común
    servicios = []

    if en_comun & FLETE:
        servicios.append("Flete")
    if en_comun & SEGURO:
        servicios.append("Seguro")
    if en_comun & DESPACHO:
        servicios.append("Despacho aduanal")
    if en_comun & ALMACENAJE:
        servicios.append("Almacenaje")

    if en_comun == 0:
        print("En común: Ninguno")
    else:
        print("En común:", ", ".join(servicios))
