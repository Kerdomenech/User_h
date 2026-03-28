# Lista global para almacenar los productos
inventario = []


#TASK 2: Captura datos y los guarda en un diccionario dentro de la lista

def agregar_producto():
    
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio unitario: "))
    cantidad = int(input("Cantidad en stock: "))
    
    # Creamos el diccionario del producto
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    
    # Lo agregamos a la lista global
    inventario.append(producto)
    print(f" {nombre} agregado con éxito.")

#TASK 3: Recorre la lista con un for para buscar datos
def mostrar_inventario():
    
    if not inventario:
        print(" El inventario está vacío.")
    else:
        print(" LISTA DE PRODUCTOS ")
        for p in inventario:
            print(f"Producto: {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}")

#TASK 4: Calcula el valor total y la cantidad de registros
def calcular_estadisticas():

    if not inventario:
        print(" No hay datos para calcular estadísticas.")
        return

    valor_total_stock = 0
    cantidad_total_items = len(inventario)

    for p in inventario:
        # Sumatoria de (precio * cantidad) de cada producto
        valor_total_stock += (p['precio'] * p['cantidad'])

    print("ESTADÍSTICAS DEL INVENTARIO ")
    print(f"Total de productos registrados: {cantidad_total_items}")
    print(f"Valor total del inventario: ${valor_total_stock}")

#Task 1 ejecucion del menu 
def ejecutar_menu():
    ejecutando = True

    while ejecutando:
        print(" MENÚ DE GESTIÓN DE INVENTARIO ")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadísticas")
        print("4. Salir")
        
        opcion = input("Elija una opción (1-4): ")

        # TASK 1: Validación con condicionales if/elif/else
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            calcular_estadisticas()
        elif opcion == "4":
            print("Saliendo....¡Hasta luego!")
            ejecutando = False
        else:
            print(" Opción inválida. Por favor, intente de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    ejecutar_menu()

