def agregar_producto(inventario, n, p, c):
    """Agrega un diccionario a la lista."""
    inventario.append({"nombre": n, "precio": p, "cantidad": c})

def buscar_producto(inventario, nombre_buscar):
    """Busca un producto sin usar break."""
    resultado = None
    for p in inventario:
        if p['nombre'].lower() == nombre_buscar.lower():
            resultado = p
    return resultado

def calcular_estadisticas(inventario):
    """TASK 3: Procesa métricas sin loops infinitos."""
    if not inventario:
        return None

    unidades_totales = 0
    valor_total = 0
    # Inicializamos con el primer elemento para comparar
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