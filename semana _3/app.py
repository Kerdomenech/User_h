import servicios
import archivos

def ejecutar_sistema():
    inventario = []
    programa_activo = True

    while programa_activo:
        print("")
        print("INVENTARIO RIWI")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Estadisticas")
        print("7. Guardar CSV")
        print("8. Cargar CSV")
        print("9. Salir")
        print("")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            servicios.agregar_producto(inventario, nombre, precio, cantidad)
            print("Producto agregado correctamente.")
        elif opcion == "2":
            servicios.mostrar_inventario(inventario)
        elif opcion == "3":
            nombre = input("Nombre del producto a buscar: ")
            resultado = servicios.buscar_producto(inventario, nombre)
            if resultado is None:
                print("Producto no encontrado.")
            else:
                print("Producto: " + resultado["nombre"] + " | Precio: " + str(resultado["precio"]) + " | Cantidad: " + str(resultado["cantidad"]))
        elif opcion == "4":
            nombre = input("Nombre del producto a actualizar: ")
            nuevo_precio = float(input("Nuevo precio: "))
            nueva_cantidad = int(input("Nueva cantidad: "))
            servicios.actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)
        elif opcion == "5":
            nombre = input("Nombre del producto a eliminar: ")
            servicios.eliminar_producto(inventario, nombre)
        elif opcion == "6":
            resultado = servicios.calcular_estadisticas(inventario)
            if resultado is None:
                print("No hay datos para calcular estadisticas.")
            else:
                u, v, caro, stock = resultado
                print("Total de unidades: " + str(u))
                print("Valor total del inventario: $" + str(v))
                print("Producto mas caro: " + caro["nombre"] + " | Precio: $" + str(caro["precio"]))
                print("Producto con mayor stock: " + stock["nombre"] + " | Cantidad: " + str(stock["cantidad"]))
        elif opcion == "7":
            archivos.guardar_csv(inventario, "inventario.csv")
        elif opcion == "8":
            nuevos, errores = archivos.cargar_csv("inventario.csv")
            if nuevos:
                print("Se encontraron " + str(len(nuevos)) + " productos. " + str(errores) + " filas invalidas.")
                confirmar = input("Sobrescribir inventario actual? (S/N): ")
                if confirmar == "S":
                    inventario = nuevos
                    print("Inventario reemplazado correctamente.")
                else:
                    inventario.extend(nuevos)
                    print("Productos fusionados correctamente.")
        elif opcion == "9":
            print("Cerrando sistema... Hasta luego.")
            programa_activo = False
        else:
            print("Opcion no valida. Intente de nuevo.")

ejecutar_sistema()
