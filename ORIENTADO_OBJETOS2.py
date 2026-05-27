from dataclasses import dataclass

@dataclass
class Venta:
    articulo: str
    cantidad: int
    precio_unitario: float

    def calcular_subtotal(self) -> float:
        return self.cantidad * self.precio_unitario


def leer_numero(mensaje, tipo=float, permite_cero=False):
  
    while True:
        try:
            valor = tipo(input(mensaje))
            
            # Validación según el enunciado
            if valor < 0:
                print("Error: El valor no puede ser negativo.")
                continue
            if not permite_cero and valor == 0:
                print("Error: El valor debe ser mayor a cero.")
                continue
                
            return valor
        except ValueError:
            print("Error: Entrada inválida. Ingrese un número válido.")


def registrar_venta() -> Venta:
 
    articulo = input("Digite el nombre del artículo: ").strip()
    while not articulo:
        print("El nombre del artículo no puede estar vacío.")
        articulo = input("Digite el nombre del artículo: ").strip()

    cantidad = leer_numero("Digite la cantidad vendida: ", int, permite_cero=False)
    
    
    precio = leer_numero("Digite el precio unitario: ", float, permite_cero=False)
    
    return Venta(articulo, cantidad, precio)


def calcular_totales(ventas: list[Venta]) -> tuple[int, float]:

    total_articulos = sum(v.cantidad for v in ventas)
    total_dinero = sum(v.calcular_subtotal() for v in ventas)
    return total_articulos, total_dinero


def main():
    ventas: list[Venta] = []
    
    print("--- SISTEMA DE GESTIÓN DE VENTAS DIARIAS ---")
    cantidad_ventas = leer_numero("Digite la cantidad de ventas a registrar hoy: ", int, permite_cero=False)
    
    for i in range(cantidad_ventas):
        print(f"\nRegisrando Venta {i + 1}:")
        ventas.append(registrar_venta())
        
    
    total_articulos, total_recaudado = calcular_totales(ventas)
    

    print("\n" + "="*40)
    print("      RESUMEN DE VENTAS DEL DÍA")
    print("="*40)
    print(f"Total de artículos vendidos: {total_articulos}")
    print(f"Total de dinero recaudado:   ${total_recaudado:,.2f}")
    print("="*40)

if __name__ == "__main__":
    main()
