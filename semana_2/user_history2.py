
# Lista global para almacenar los productos
inventario = []



# TASK 2: Captura datos y los guarda en un diccionario dentro de la lista

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
    print(nombre + " agregado con exito.")



# TASK 3: Recorre la lista con un for para mostrar los datos

def mostrar_inventario():
    if not inventario:
        print("El inventario esta vacio.")
    else:
        print("LISTA DE PRODUCTOS")
        for p in inventario:
            print("Producto: " + p["nombre"] + " | Precio: " + str(p["precio"]) + " | Cantidad: " + str(p["cantidad"]))


# TASK 4: Calcula el valor total y la cantidad de registros
def calcular_estadisticas():
    if not inventario:
        print("No hay datos para calcular estadisticas.")
        return

    valor_total_stock = 0
    cantidad_total_items = len(inventario)

    for p in inventario:
        # Sumatoria de (precio * cantidad) de cada producto
        valor_total_stock += p["precio"] * p["cantidad"]

    print("ESTADISTICAS DEL INVENTARIO")
    print("Total de productos registrados: " + str(cantidad_total_items))
    print("Valor total del inventario: $" + str(valor_total_stock))



# TASK 1: Menu principal con while y condicionales if/elif/else
def ejecutar_menu():
    ejecutando = True

    while ejecutando:
        print("")
        print("MENU DE GESTION DE INVENTARIO")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadisticas")
        print("4. Salir")
        print("")

        opcion = input("Elija una opcion (1-4): ")

        # Validacion con condicionales if/elif/else
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            calcular_estadisticas()
        elif opcion == "4":
            print("Saliendo... Hasta luego!")
            ejecutando = False
        else:
            print("Opcion invalida. Por favor, intente de nuevo.")



# Punto de ejecucion del programa

ejecutar_menu()


# TASK 5 - Comentario general del programa
# Este programa gestiona un inventario de productos usando una lista de diccionarios.
# El usuario puede agregar productos, ver todos los registros, calcular estadisticas del inventario,o salir.
# El menu se mantiene activo con un bucle while hasta que el usuario elige salir. 
# Cada opcion del menu esta organizada en su propia funcion para mantener el codigo limpio y legible.