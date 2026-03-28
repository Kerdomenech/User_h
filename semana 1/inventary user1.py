#TASK 2
#  Fase de Entrada: Captura de información
nombre = input("Ingrese el nombre del producto: ")

# usamos a float e int para ingresar un dato (sin validación por comando)
precio = float(input("Ingrese el precio unitario: "))
cantidad = int(input("Ingrese la cantidad: "))

# Cálculo del costo total
costo_total = precio * cantidad

#TASK 3
# Fase de Salida: Resumen detallado

print("INFORME DE PROCESAMIENTO")
print(f"Producto: {nombre}")
print(f"Precio Unitario: {precio}")
print(f"Cantidad: {cantidad}")
print(f"COSTO TOTAL: {costo_total}")
