
print("ACTIVIDAD 4 - EJERCICIO 10")
print("Nombre: Yaretzy Tudon Escamilla")
print("Matrícula: AL07029520")
print("Permisos del sistema de pedidos")

# Crear constantes
VER = 1 << 0
CREAR = 1 << 1
APROBAR = 1 << 2
EXPORTAR = 1 << 3

# Crear permisos según el puesto
puesto = int(input("Puesto (1 Practicante, 2 Vendedor, 3 Gerente): "))

if puesto == 1:
    permisos = VER
elif puesto == 2:
    permisos = VER | CREAR
elif puesto == 3:
    permisos = VER | CREAR | APROBAR | EXPORTAR
else:
    permisos = 0
    print("Puesto no válido: sin permisos")

# Agregar permiso de exportación
capacitacion = input("¿Tomó capacitación? (si/no): ").lower()

if capacitacion == "si":
    permisos = permisos | EXPORTAR

# Quitar permiso de aprobación por vacaciones
vacaciones = input("¿Está de vacaciones? (si/no): ").lower()

if vacaciones == "si":
    permisos = permisos & ~APROBAR

# Mostrar permisos
print("Permisos finales:", format(permisos, "04b"), permisos)

# Revisar permiso de exportación
if permisos & EXPORTAR:
    print("Puede firmar pedimentos de exportación")
else:
    print("No puede firmar pedimentos de exportación")

# Revisar permisos para liberar pedidos internacionales
REQUERIDOS = CREAR | EXPORTAR

if (permisos & REQUERIDOS) == REQUERIDOS:
    print("Puede liberar pedidos internacionales")
else:
    faltan = REQUERIDOS & ~permisos
    print("No puede liberar pedidos internacionales")
    print("Faltan:", format(faltan, "04b"))

    if faltan & CREAR:
        print("Falta permiso para crear pedidos")
    if faltan & EXPORTAR:
        print("Falta permiso de exportación")
