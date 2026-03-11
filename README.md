# Venta de Artículos Deportivos

Me contrataron en una empresa para desarrollar una aplicación software para una empresa que permita la administración del registro de la venta de sus artículos, además de registrar el cálculo de las ventas generadas por día; el software también debe mostrar el total del dinero recaudado al final del día.

## Restricciones

- El sistema solo registra ventas realizadas durante un mismo día laboral.
- No se permite ingresar cantidades negativas ni valores de precio menores o iguales a cero.
- La cantidad vendida debe ser un número entero positivo.
- El sistema no gestionará inventario ni controlará stock, únicamente registrará ventas del día.
- No se permite modificar una venta ya registrada (solo se registran nuevas ventas).
- El cálculo del total diario se realiza únicamente con las ventas ingresadas en la sesión actual donde se calculara la cantidad de articulos por su respectivo precio unitario.
- El sistema funciona de manera local y no requiere conexión a internet.

---

# Historia de usuario

**Título:** Registro diario de ventas de artículos deportivos.

**Como:** Vendedor de la tienda  

**Quiero:** Registrar cada venta realizada durante el día (artículo, cantidad y precio)  

**Para:** Obtener al final del día el total de artículos vendidos y el total de dinero recaudado.

## Descripción

El sistema debe permitir ingresar cada venta que se realice durante la jornada. Por cada venta se debe registrar el artículo vendido, la cantidad y su precio unitario. Al finalizar el día, el sistema debe calcular automáticamente:

- El total de artículos vendidos en el día.
- El total de dinero recaudado en el día.

## Requisitos

El sistema debe permitir:

- Registrar múltiples ventas durante el día.
- Acumular la cantidad total de artículos vendidos.
- Calcular el total de dinero generado por todas las ventas.
- Mostrar un resumen final con el total de artículos vendidos y el total recaudado.

---

# Criterios de aceptación

- El sistema permite registrar cada venta ingresando nombre del artículo, cantidad vendida y precio unitario.
- El sistema permitirá acumular la cantidad total de artículos vendidos durante el día.
- El sistema calcula correctamente el total de dinero recaudado sumando todas las ventas registradas.
- Al finalizar la jornada, el sistema muestra en pantalla:
  - Total de artículos vendidos.
  - Total de dinero recaudado en el día.

---

# Diagrama UML

<img width="886" height="430" alt="image" src="https://github.com/user-attachments/assets/4a5c8aaf-37f8-4fda-92f6-c01bb7335603" />


---

# Caso de uso extendido

**Nombre:** Registrar Ventas Diarias de Artículos Deportivos  

**Actor:** Vendedor  

**Propósito:** Registrar cada venta realizada durante el día y calcular al final el total de artículos vendidos y el total de dinero recaudado.

## Curso de eventos

1. El vendedor inicia el registro de ventas del día.
2. El sistema solicita la cantidad de ventas que se realizarán durante la jornada.
3. Para cada venta:
   - El vendedor ingresa el nombre del artículo.
   - El vendedor ingresa la cantidad vendida.
   - El vendedor ingresa el precio unitario.
   - El sistema calcula el subtotal de la venta:  
     **cantidad × precio unitario**
   - El sistema acumula:
     - La cantidad total de artículos vendidos.
     - El total de dinero recaudado.
4. Al finalizar el registro de todas las ventas, el sistema muestra:
   - Total de artículos vendidos en el día.
   - Total de dinero recaudado en el día.

**Postcondición:**  
El sistema ha calculado correctamente el total de artículos vendidos y el total de ventas generadas durante el día.

---

# Diagrama de flujo

<img width="1033" height="1253" alt="image" src="https://github.com/user-attachments/assets/99c10a80-d982-48f5-b5a6-0f3ef959ef25" />


# Pseudocódigo
INICIO

Definir articulo Como Cadena
Definir cantidad, totalArticulos Como Entero
Definir precio, totalDinero, totalVenta Como Real
Definir continuar Como Cadena

totalArticulos <- 0
totalDinero <- 0

Repetir
Escribir "Ingrese el nombre del artículo:"
Leer articulo

Escribir "Ingrese la cantidad vendida:"
Leer cantidad

Mientras cantidad <= 0 Hacer
Escribir "Error: la cantidad debe ser un número entero positivo"
Leer cantidad
FinMientras
Escribir "Ingrese el precio unitario:"
Leer precio

Mientras precio <= 0 Hacer
Escribir "Error: el precio debe ser mayor que cero"
Leer precio
FinMientras

totalVenta <- cantidad * precio

totalArticulos <- totalArticulos + cantidad
totalDinero <- totalDinero + totalVenta

Escribir "¿Desea registrar otra venta? (SI/NO)"
Leer continuar

Hasta Que continuar = "NO"

Escribir "Resumen del día"
Escribir "Total de artículos vendidos: ", totalArticulos
Escribir "Total de dinero recaudado: ", totalDinero

FIN
