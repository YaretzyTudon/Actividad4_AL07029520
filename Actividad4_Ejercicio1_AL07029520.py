print("ACTIVIDAD 4 - EJERCICIO 1")
print("Nombre: Yaretzy Tudon Escamilla")
print("Matrícula: AL07029520")

def respuesta_si_no(pregunta):
    respuesta = input(pregunta + " (si/no): ").lower()
    while respuesta not in ("si", "no"):
        print("Escribe si o no.")
        respuesta = input(pregunta + " (si/no): ").lower()
    return respuesta == "si"

factura = respuesta_si_no("¿Trae factura comercial?")
pedimento = respuesta_si_no("¿Trae pedimento?")
impuestos = respuesta_si_no("¿Están pagados los impuestos?")
mercancia = respuesta_si_no("¿Coincide la mercancía?")
valor = float(input("Valor de la mercancía: $"))

if factura and pedimento and impuestos and mercancia:
    print("EMBARQUE LIBERADO")

    if valor > 100000:
        print("Avisar al gerente de logística")
    else:
        print("No requiere aviso")
else:
    print("EMBARQUE DETENIDO")
    pendientes = 0

    if not factura:
        print("Falta factura")
        pendientes += 1

    if not pedimento:
        print("Falta pedimento")
        pendientes += 1

    if not impuestos:
        print("Falta pagar impuestos")
        pendientes += 1

    if not mercancia:
        print("La mercancía no coincide")
        pendientes += 1

    print("Requisitos pendientes:", pendientes)