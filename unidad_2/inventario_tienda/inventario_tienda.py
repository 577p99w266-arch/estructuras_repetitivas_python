class InventarioTienda:
    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self.productos = []

    def agregar_producto(self, nombre, precio, cantidad):
        if not nombre.strip() or precio <= 0 or cantidad <= 0:
            print("El nombre, el precio y la cantidad deben ser válidos y positivos.")
            return

        for producto in self.productos:
            if producto["nombre"].lower() == nombre.lower():
                print("Ese producto ya existe. Usa otro nombre.")
                return

        self.productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
        print(f"Producto '{nombre}' agregado correctamente.")

    def vender_producto(self, nombre, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser positiva.")
            return

        for producto in self.productos:
            if producto["nombre"].lower() == nombre.lower():
                if producto["cantidad"] < cantidad:
                    print(f"Stock insuficiente. Solo hay {producto['cantidad']} unidades.")
                    return
                producto["cantidad"] -= cantidad
                print(f"Venta realizada: {cantidad} unidad(es) de {producto['nombre']}.")
                return

        print("El producto no existe en el inventario.")

    def mostrar_inventario(self):
        print(f"\nInventario de {self.nombre_tienda}:")
        if not self.productos:
            print("No hay productos registrados.")
            return

        for producto in self.productos:
            print(f"- {producto['nombre']}: ${producto['precio']:.2f} | "
                  f"Cantidad: {producto['cantidad']}")

    def producto_mas_caro(self):
        if not self.productos:
            return None
        producto = max(self.productos, key=lambda p: p["precio"])
        return producto["nombre"], producto["precio"]


def leer_numero_positivo(mensaje, tipo):
    while True:
        try:
            valor = tipo(input(mensaje))
            if valor > 0:
                return valor
            print("Ingresa un valor mayor que cero.")
        except ValueError:
            print("Ingresa un número válido.")


def main():
    tienda = InventarioTienda("Mi tienda")

    while True:
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Vender producto")
        print("3. Ver inventario")
        print("4. Consultar producto más caro")
        print("5. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre del producto: ").strip()
            if not nombre:
                print("El nombre no puede quedar vacío.")
                continue
            precio = leer_numero_positivo("Precio: $", float)
            cantidad = leer_numero_positivo("Cantidad: ", int)
            tienda.agregar_producto(nombre, precio, cantidad)
        elif opcion == "2":
            nombre = input("Producto que deseas vender: ").strip()
            if not nombre:
                print("Escribe el nombre del producto.")
                continue
            cantidad = leer_numero_positivo("Unidades a vender: ", int)
            tienda.vender_producto(nombre, cantidad)
        elif opcion == "3":
            tienda.mostrar_inventario()
        elif opcion == "4":
            resultado = tienda.producto_mas_caro()
            if resultado is None:
                print("No hay productos en el inventario.")
            else:
                nombre, precio = resultado
                print(f"Producto más caro: {nombre} (${precio:.2f})")
        elif opcion == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
