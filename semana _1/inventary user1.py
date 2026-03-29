#  Sistema de Registro de Inventario

#TASK 2 DATOS
# Solicitar el nombre del producto
nombre = input("Ingrese el nombre del producto: ")

# Solicitar el precio y convertirlo a numero decimal
precio = float(input("Ingrese el precio unitario: "))

# Solicitar la cantidad y convertirla a numero entero
cantidad = int(input("Ingrese la cantidad: "))



# TASK 3 - Fase de Procesamiento: Calcular el costo total

# Multiplicamos el precio por la cantidad para obtener el costo total
costo_total = precio * cantidad



# TASK 4 - Fase de Salida: Mostrar resultados en consola

# Mostramos un resumen con todos los datos y el resultado
print("INFORME DE PROCESAMIENTO")
print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")


# TASK 5 - Comentario general del programa

# Este programa solicita al usuario el nombre, precio y cantidad de un producto.
# Luego calcula el costo total multiplicando el precio por la cantidad, y muestra un resumen con todos los
# datos en consola.