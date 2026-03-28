import csv

def guardar_csv(inventario, ruta):
    """TASK 4: Guarda los datos en un archivo."""
    if not inventario:
        print("⚠️ Inventario vacío, nada que guardar.")
        return

    try:
        with open(ruta, mode='w', newline='', encoding='utf-8') as f:
            escritor = csv.DictWriter(f, fieldnames=['nombre', 'precio', 'cantidad'])
            escritor.writeheader()
            escritor.writerows(inventario)
            print(f"✅ Guardado en: {ruta}")
    except Exception as e:
        print(f"❌ Error al escribir archivo: {e}")

def cargar_csv(ruta):
    """TASK 5: Carga y valida filas."""
    datos_nuevos = []
    errores = 0
    try:
        with open(ruta, mode='r', encoding='utf-8') as f:
            lector = csv.DictReader(f)
            for fila in lector:
                try:
                    p = float(fila['precio'])
                    c = int(fila['cantidad'])
                    if p >= 0 and c >= 0:
                        datos_nuevos.append({"nombre": fila['nombre'], "precio": p, "cantidad": c})
                    else:
                        errores += 1
                except:
                    errores += 1
        return datos_nuevos, errores
    except FileNotFoundError:
        print("❌ El archivo no existe.")
        return [], 0