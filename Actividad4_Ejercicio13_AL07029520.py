
# Ejercicio 13 - Cotizaciones de proveedores

cotizaciones = []

presupuesto = 5000

for i in range(5):
    precio = int(input(f"Ingresa la cotizacion {i + 1}: "))
    cotizaciones.append(precio)

print("\nCotizaciones originales:", cotizaciones)

total = len(cotizaciones)

for vuelta in range(total - 1):
    for lugar in range(total - 1 - vuelta):
        precio_izquierda = cotizaciones[lugar]
        precio_derecha = cotizaciones[lugar + 1]

        if precio_izquierda > precio_derecha:
            cotizaciones[lugar] = precio_derecha
            cotizaciones[lugar + 1] = precio_izquierda

    print(f"Vuelta {vuelta + 1}: {cotizaciones}")

print("\nCotizacion mas barata:", cotizaciones[0])
print("Cotizacion mas cara:", cotizaciones[-1])

if cotizaciones[0] <= presupuesto:
    print("Se aprueba la compra")
else:
    print("Se deben buscar nuevas cotizaciones")
