articulos = []
cantidades = []
precios = []

numero_ventas = int(input("Digite el número de ventas del día: "))

for i in range(numero_ventas):
    print(f"\nVenta {i + 1}:")

    articulo = input("Digite el nombre del artículo: ")

    cantidad = int(input("Digite la cantidad vendida: "))
    while cantidad <= 0:
        print("Error: la cantidad debe ser un número entero positivo")
        cantidad = int(input("Digite nuevamente la cantidad: "))

    precio = float(input("Digite el precio unitario: "))
    while precio <= 0:
        print("Error: el precio debe ser mayor que cero")
        precio = float(input("Digite nuevamente el precio: "))

    articulos.append(articulo)
    cantidades.append(cantidad)
    precios.append(precio)

total_articulos = 0
total_dinero = 0

for i in range(numero_ventas):
    total_articulos = total_articulos + cantidades[i]
    total_dinero = total_dinero + (cantidades[i] * precios[i])

print("\nResumen del día")
print("Total de artículos vendidos:", total_articulos)
print("Total de dinero recaudado:", total_dinero)