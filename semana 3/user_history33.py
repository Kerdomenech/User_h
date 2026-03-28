import user_history31
import user_history32

def ejecutar_sistema():
    inventario = []
    programa_activo = True  # Bandera en lugar de while True

    while programa_activo:
        print("\n--- INVENTARIO RIWI ---")
        print("1. Agregar | 2. Mostrar | 3. Estadísticas | 4. Guardar | 5. Cargar | 6. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                n = input("Nombre: ")
                p = float(input("Precio: "))
                c = int(input("Cantidad: "))
                servicios.agregar_producto(inventario, n, p, c)
            except ValueError:
                print(" Error: Use números para precio y cantidad.")

        elif opcion == "2":
            if not inventario:
                print("El inventario está vacío.")
            for p in inventario:
                print(f"Producto: {p['nombre']} | $: {p['precio']} | Cant: {p['cantidad']}")

        elif opcion == "3":
            res = servicios.calcular_estadisticas(inventario)
            if res:
                u, v, caro, stock = res
                print(f"Total Unidades: {u}\nValor Total: ${v}\nMás Caro: {caro['nombre']}")
            else:
                print("No hay datos.")

        elif opcion == "4":
            archivos.guardar_csv(inventario, "inventario.csv")

        elif opcion == "5":
            nuevos, err = archivos.cargar_csv("inventario.csv")
            if nuevos:
                print(f"Se encontraron {len(nuevos)} productos. {err} errores omitidos.")
                confirmar = input("¿Sobrescribir actual? (S/N): ").lower()
                if confirmar == "s":
                    inventario = nuevos
                else:
                    inventario.extend(nuevos) # Fusión simple

        elif opcion == "6":
            print("Cerrando sistema...")
            programa_activo = False  # Cambiamos la bandera para salir del ciclo

        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    ejecutar_sistema()