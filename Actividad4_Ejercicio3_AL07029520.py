print("ACTIVIDAD 4 - EJERCICIO 3")
print("Nombre: Yaretzy Tudon Escamilla")
print("Matrícula: AL07029520")

producto = input("Nombre del producto: ")

restringido = input("¿Está restringido? (si/no): ").lower() == "si"
tiene_permiso = input("¿Tiene permiso? (si/no): ").lower() == "si"
vigente = input("¿El permiso está vigente? (si/no): ").lower() == "si"
destino = input("¿El país tiene restricciones? (si/no): ").lower() == "si"

kilos = float(input("Peso en kg: "))

permiso_valido = tiene_permiso and vigente

puede_exportar = (not restringido or permiso_valido) and not destino

if puede_exportar:
    print("Se puede exportar:", producto)

    if restringido and kilos > 1000:
        print("Necesita inspección previa")

else:
    print("No se puede exportar")

    if destino:
        print("Motivo: destino restringido")

    elif restringido and not tiene_permiso:
        print("Motivo: no hay permiso")

    elif restringido and tiene_permiso and not vigente:
        print("Motivo: permiso vencido")