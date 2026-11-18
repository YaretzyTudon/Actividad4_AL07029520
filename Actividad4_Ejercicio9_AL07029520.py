
print("ACTIVIDAD 4 - EJERCICIO 9")
print("Nombre: Yaretzy Tudon Escamilla")
print("Matrícula: AL07029520")
print("Requisitos de aduana")

# Crear constantes con desplazamiento
FACTURA = 1 << 0
PEDIMENTO = 1 << 1
IMPUESTOS = 1 << 2
MERCANCIA = 1 << 3

TODOS = FACTURA | PEDIMENTO | IMPUESTOS | MERCANCIA

# Iniciar código
codigo = 0

# Preguntar los requisitos
if input("¿Tiene factura? (si/no): ").lower() == "si":
    codigo = codigo | FACTURA

if input("¿Tiene pedimento? (si/no): ").lower() == "si":
    codigo = codigo | PEDIMENTO

if input("¿Tiene impuestos pagados? (si/no): ").lower() == "si":
    codigo = codigo | IMPUESTOS

if input("¿Coincide la mercancía? (si/no): ").lower() == "si":
    codigo = codigo | MERCANCIA

# Mostrar código
print("Código:", format(codigo, "04b"), codigo)

# Revisar si está completo
if (codigo & TODOS) == TODOS:
    print("EMBARQUE LIBERADO")

else:
    faltan = ~codigo & TODOS

    print("EMBARQUE DETENIDO")
    print("Faltan:", format(faltan, "04b"))

    if faltan & FACTURA:
        print("Falta factura")
    if faltan & PEDIMENTO:
        print("Falta pedimento")
    if faltan & IMPUESTOS:
        print("Falta pago de impuestos")
    if faltan & MERCANCIA:
        print("Falta revisar mercancía")
