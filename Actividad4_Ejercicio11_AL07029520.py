
# Nombre: Yaretzy Tudon Escamilla
# Matricula: AL07029520
# Ejercicio 11: Revision de pedido y reporte de ventas

catalogo = ["CAFE", "TEQUILA", "MIEL", "AGUACATE", "ACIDO SULFURICO"]
restringidos = ["ACIDO SULFURICO", "MERCURIO", "PIROTECNIA"]
tmec = ["MEXICO", "ESTADOS UNIDOS", "CANADA"]
ventas = [120, 95, 140, 160, 110, 175]

producto = input("Escribe el producto: ").upper()
pais = input("Escribe el pais destino: ").upper()
meses = int(input("Cuantos meses deseas consultar (1-6)? "))

# Revisar catalogo
if producto not in catalogo:
    print("El producto no esta en el catalogo.")
else:
    print("El producto si esta en el catalogo.")

    # Revisar productos restringidos
    if producto in restringidos:
        print("Necesita permiso especial para exportar.")
    else:
        print("Se puede exportar sin permiso.")

    # Revisar tratado comercial
    if pais in tmec:
        print("Aplica T-MEC. Arancel 0%.")
    else:
        print("No aplica T-MEC. Se cobra arancel general.")

# Reporte de ventas
if meses < 1 or meses > 6:
    print("Error: escribe un numero de meses entre 1 y 6.")
else:
    print("Primeros meses:", ventas[:meses])
    print("Ultimos meses:", ventas[-meses:])
    print("Primer trimestre:", ventas[:3])
    print("Segundo trimestre:", ventas[3:6])
