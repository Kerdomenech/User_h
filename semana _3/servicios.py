#Funcion para añadir al inventario
def agregar_producto(inventario, n, p, c):
    inventario.append({"nombre": n, "precio": p, "cantidad": c})

# funcion buscar un producto
def buscar_producto(inventario, nombre_buscar):
    resultado = None
    for p in inventario:
        if p['nombre'].lower() == nombre_buscar.lower():
            resultado = p
    return resultado

#TASK 3: loops para la añadir productos al inv
def calcular_estadisticas(inventario):
    if not inventario:
        return None

    #lista
    unidades_totales = 0
    valor_total = 0
    
    p_caro = inventario[0]
    p_stock = inventario[0]
    
    for p in inventario:
        unidades_totales += p['cantidad']
        valor_total += (p['precio'] * p['cantidad'])
        
        if p['precio'] > p_caro['precio']:
            p_caro = p
        if p['cantidad'] > p_stock['cantidad']:
            p_stock = p
            
    return (unidades_totales, valor_total, p_caro, p_stock)

#Muestra todos los productos del inventario
def mostrar_inventario(inventario):
    if not inventario:
        print("El inventario esta vacio.")
        return
    for p in inventario:
        print("Producto: " + p["nombre"] + " | Precio: " + str(p["precio"]) + " | Cantidad: " + str(p["cantidad"]))

#Actualiza el precio y/o cantidad de un producto existente
def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    producto = buscar_producto(inventario, nombre)
    if producto is None:
        print("Producto no encontrado: " + nombre)
        return
    if nuevo_precio is not None:
        producto["precio"] = nuevo_precio
    if nueva_cantidad is not None:
        producto["cantidad"] = nueva_cantidad
    print("Producto actualizado correctamente.")

#Elimina un producto de la lista por nombre
def eliminar_producto(inventario, nombre):
    producto = buscar_producto(inventario, nombre)
    if producto is None:
        print("Producto no encontrado: " + nombre)
        return
    inventario.remove(producto)
    print("Producto eliminado correctamente.")
