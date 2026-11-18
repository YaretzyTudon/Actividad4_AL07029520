
# Ejercicio 14: Ranking de vendedores del mes

vendedores = ["Sofia", "Mateo", "Valeria", "Diego", "Camila"]
ventas = [85, 120, 95, 140, 70]

print("RANKING DE VENDEDORES DEL MES")
print("Ventas iniciales:", ventas)
print("Vendedores:", vendedores)

# Ordenar de mayor a menor con metodo burbuja
for vuelta in range(4):
    for lugar in range(4 - vuelta):

        if ventas[lugar] < ventas[lugar + 1]:

            # Cambiar las ventas
            venta_temp = ventas[lugar]
            ventas[lugar] = ventas[lugar + 1]
            ventas[lugar + 1] = venta_temp

            # Cambiar tambien los vendedores
            vendedor_temp = vendedores[lugar]
            vendedores[lugar] = vendedores[lugar + 1]
            vendedores[lugar + 1] = vendedor_temp

    print("Vuelta", vuelta + 1, ":", ventas)

# Mostrar ranking final
print("\nRANKING FINAL")

for lugar in range(5):
    print(lugar + 1, vendedores[lugar], "-", ventas[lugar], "mil pesos")

    if lugar < 3:
        print("Gana bono")
    else:
        print("No gana bono")
