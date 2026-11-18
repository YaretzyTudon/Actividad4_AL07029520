print("Nombre: Yaretzy Tudon Escamilla")
print("Matrícula: AL07029520")

pais = input("País de origen: ").upper()
certificado = input("¿Tiene certificado? (si/no): ").lower() == "si"
valor = float(input("Valor de mercancía: $"))

if pais == "MEXICO":
    print("Mercancía nacional")
    print("No paga impuestos de importación")

else:
    origen_tmec = pais == "ESTADOS UNIDOS" or pais == "CANADA"

    preferencial = origen_tmec and certificado

    if preferencial:
        arancel = 0
    else:
        arancel = 15

    impuesto = valor * arancel / 100
    iva = (valor + impuesto) * 16 / 100
    total = valor + impuesto + iva

    print("Arancel:", arancel, "%")
    print("Impuesto de arancel: $", impuesto)
    print("IVA: $", iva)
    print("Total: $", total)

    if origen_tmec and not certificado:
        ahorro = valor * 15 / 100
        print("Ahorro posible: $", ahorro)