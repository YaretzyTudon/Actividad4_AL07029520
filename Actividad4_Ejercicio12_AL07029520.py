
# Nombre: Yaretzy Tudon Escamilla
# Matricula: AL07029520
# Ejercicio 12: Precios del Buen Fin

productos = ["Cafe", "Tequila", "Miel", "Mezcal", "Cacao"]
precios = [450, 1200, 300, 980, 150]

descuento = float(input("Escribe el porcentaje de descuento: "))
consulta = input("Que producto desea consultar? ").capitalize()

# Crear una copia real
promocion = precios[:]

# Aplicar descuento
for i in range(len(promocion)):
    promocion[i] = promocion[i] - (promocion[i] * descuento / 100)

# Solo los primeros tres productos
promocion = promocion[:3]
del promocion[3:]

# Buscar el precio mas alto
mayor = promocion[0]
posicion_mayor = 0

for i in range(len(promocion)):
    if promocion[i] > mayor:
        mayor = promocion[i]
        posicion_mayor = i

print("\nPrecios originales:", precios)
print("Precios de promocion:", promocion)
print("Producto mas caro en promocion:", productos[posicion_mayor])
print("Precio mas alto:", mayor)

# Consultar producto
if consulta not in productos:
    print("El producto no esta en el catalogo.")
else:
    posicion = productos.index(consulta)
    print("Precio normal:", precios[posicion])

    if consulta in productos[:3]:
        print("Precio Buen Fin:", promocion[posicion])
    else:
        print("Este producto no entra a la promocion.")
        print("Se cobra el precio normal.")
