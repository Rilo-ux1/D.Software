class Venta:

    def __init__(self, articulo, cantidad, precio_unitario):
        self.articulo = articulo
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    def subtotal(self):
        return self.cantidad * self.precio_unitario


def main():

    ventas = []

    cantidad_ventas = int(input("Digite la cantidad de ventas del día: "))

    for i in range(cantidad_ventas):

        print(f"\nVenta {i + 1}:")

        articulo = input("Digite el nombre del artículo: ")

        cantidad = int(input("Digite la cantidad vendida: "))
        while cantidad <= 0:
            print("Error: la cantidad debe ser un número positivo")
            cantidad = int(input("Digite nuevamente la cantidad: "))

        precio = float(input("Digite el precio unitario: "))
        while precio <= 0:
            print("Error: el precio debe ser mayor que cero")
            precio = float(input("Digite nuevamente el precio: "))

        venta = Venta(articulo, cantidad, precio)
        ventas.append(venta)

    total_articulos = sum(
        venta.cantidad
        for venta in ventas
    )

    total_dinero = sum(
        venta.subtotal()
        for venta in ventas
    )

    print("\nResumen del día")
    print(f"Total de artículos vendidos: {total_articulos}")
    print(f"Total de dinero recaudado: {total_dinero}")


if __name__ == "__main__":
    main()