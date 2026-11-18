print("ACTIVIDAD 4 - EJERCICIO 4")
print("Nombre: Yaretzy Tudon Escamilla")
print("Matrícula: AL07029520")

valor = float(input("Valor del embarque: $"))

documentos = input("¿Documentos completos? (si/no): ").lower() == "si"
primera_vez = input("¿Primera importación? (si/no): ").lower() == "si"
certificada = input("¿Empresa certificada? (si/no): ").lower() == "si"
perecedera = input("¿Mercancía perecedera? (si/no): ").lower() == "si"

candidato = valor > 50000 or primera_vez

rojo = (not documentos) or (candidato and not certificada)

if rojo:
    color = "ROJO"

    if perecedera:
        dias = 1
        print("Revisión prioritaria")
    else:
        dias = 3

else:
    color = "VERDE"
    dias = 0

almacenaje = dias * 500

print("Semáforo:", color)
print("Días en aduana:", dias)
print("Costo de almacenaje: $", almacenaje)