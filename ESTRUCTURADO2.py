def main():

    ventas = []

    numero_ventas = int(input("Digite el número de ventas del día: "))

    for i in range(numero_ventas):
        print(f"\nVenta {i + 1}:")

        articulo = input("Nombre del artículo: ")

        cantidad = int(input("Cantidad vendida: "))
        while cantidad <= 0:
            print("Error: la cantidad debe ser positiva")
            cantidad = int(input("Cantidad vendida: "))

        precio = float(input("Precio unitario: "))
        while precio <= 0:
            print("Error: el precio debe ser mayor que cero")
            precio = float(input("Precio unitario: "))

        venta = {
            "articulo": articulo,
            "cantidad": cantidad,
            "precio": precio
        }

        ventas.append(venta)

    total_articulos = 0
    total_dinero = 0

    for venta in ventas:
        total_articulos += venta["cantidad"]
        total_dinero += venta["cantidad"] * venta["precio"]

    print("\nResumen del día")
    print("Total de artículos vendidos:", total_articulos)
    print("Total de dinero recaudado:", total_dinero)


if __name__ == "__main__":
    main()