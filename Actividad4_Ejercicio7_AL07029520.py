
print("ACTIVIDAD 4 - EJERCICIO 7")
print("Nombre: Yaretzy Tudon Escamilla")
print("Matrícula: AL07029520")
print("Pedidos que se duplican")

# Pedir información
cajas = int(input("Cajas del pedido de prueba: "))
meses = int(input("Cantidad de meses: "))

# Duplicar el pedido usando desplazamiento
pedido_final = cajas << meses

# Comprobar el resultado
comprobacion = cajas * (2 ** meses)

# Mostrar los pedidos en binario
print("Pedido inicial:", format(cajas, "b"))
print("Pedido final:", format(pedido_final, "b"))
print("Total de cajas:", pedido_final)

# Repartir las cajas
monterrey = pedido_final >> 1
guadalajara = pedido_final >> 2
cdmx = pedido_final >> 3

# Calcular las cajas sobrantes
reserva = pedido_final - monterrey - guadalajara - cdmx

print("Comprobación:", comprobacion)
print("Monterrey:", monterrey)
print("Guadalajara:", guadalajara)
print("CDMX:", cdmx)
print("Reserva:", reserva)
