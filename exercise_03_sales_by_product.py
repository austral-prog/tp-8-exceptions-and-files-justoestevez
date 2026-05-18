# Ejercicio 3 - Ventas por producto


def read_sales(filename):
    """
    Lee un archivo con ventas en formato "producto:valor;producto:valor;..."
    (todo en una sola línea, los registros separados por ';') y agrupa los
    valores en una lista por producto.

    Reglas:
    - Los valores se convierten a float.
    - El orden de los montos dentro de la lista es el mismo en que aparecen
      en el archivo.
    - Los separadores ';' finales sin contenido se ignoran (es común que
      el archivo termine con ';').
    - Si el archivo no existe, propagar FileNotFoundError.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        dict[str, list[float]] - montos de venta agrupados por producto.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene: "producto1:100;producto2:200;producto1:150;"
        read_sales("ventas.txt") -> {
            "producto1": [100.0, 150.0],
            "producto2": [200.0],
        }
    """
    ventas_dict = {}
    
    with open(filename, 'r') as archivo:
        contenido = archivo.read().strip()
        
    # Cortamos el texto largo en una lista de pedacitos
    lista_de_pedacitos = contenido.split(';') 
    
    # Revisamos un pedacito a la vez
    for pedacito in lista_de_pedacitos:
        
        # if pedacito: significa "Si el pedacito NO está vacío"
        # Esto salta el último pedacito que quedó vacío por el ';' del final
        if pedacito: 
            
            # Ahora cortamos el pedacito a la mitad usando los ':'
            producto, precio_texto = pedacito.split(':')
            
            # Pasamos el precio de texto a número decimal
            monto = float(precio_texto) 
            
            # Guardamos en el diccionario (igual que el inventario)
            if producto in ventas_dict:
                ventas_dict[producto].append(monto)
            else:
                ventas_dict[producto] = [monto]
                
    return ventas_dict 

def process_sales(data):
    """
    Para cada producto del diccionario, imprime en el orden natural del dict:

        producto: ventas totales $X.XX, promedio $Y.YY

    Los valores de total y promedio deben mostrarse siempre con DOS
    decimales.

    Args:
        data: dict[str, list[float]] - salida de read_sales.

    Returns:
        None

    Ejemplo:
        process_sales({"producto1": [100.0, 150.0]})
        # imprime: "producto1: ventas totales $250.00, promedio $125.00"
    """
    for producto, lista_de_precios in data.items():
        
        # Sumamos de forma manual con un acumulador
        total_ventas = 0
        for precio in lista_de_precios:
            total_ventas += precio
            
        # Calculamos el promedio (el total dividido cuántos precios hay)
        promedio = total_ventas / len(lista_de_precios)
        
        # Imprimimos con el formato de dos decimales
        print(f"{producto}: ventas totales ${total_ventas:.2f}, promedio ${promedio:.2f}")
