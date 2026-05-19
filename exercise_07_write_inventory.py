# Ejercicio 7 - Escribir un inventario ordenado


def write_inventory(filename, inventory):
    """
    Escribe el inventario en un archivo, una línea por item, ordenadas
    alfabéticamente por nombre de item, con el formato:

        item:cantidad

    Reglas:
    - Cada línea debe terminar con "\\n".
    - Si el diccionario está vacío, el archivo se crea vacío.
    - Si el archivo ya existía, se sobreescribe.
    - La función no retorna nada (None).

    Args:
        filename: str - nombre del archivo a escribir.
        inventory: dict[str, int] - item -> cantidad.

    Returns:
        None

    Ejemplo:
        write_inventory("stock.txt", {"wood": 10, "coal": 3, "iron": 7})
        # El archivo stock.txt queda con:
        # coal:3
        # iron:7
        # wood:10
    """
    items_restantes = list(inventory.keys())
    
    # 2. Abrimos el archivo para escribir ('w')
    with open(filename, 'w') as archivo:
        
        # 3. Mientras queden cosas en la lista de pendientes...
        while len(items_restantes) > 0:
            
            # Buscamos el menor alfabéticamente
            primero_alfabeticamente = items_restantes[0]
            for item in items_restantes:
                if item < primero_alfabeticamente:
                    primero_alfabeticamente = item
            
            # Buscamos la cantidad real que tiene ese producto en el diccionario
            cantidad = inventory[primero_alfabeticamente]
            
            # 4. Lo escribimos con el formato EXACTO y el salto de línea
            archivo.write(f"{primero_alfabeticamente}:{cantidad}\n")
            
            # 5. Lo tachamos de la lista para pasar al siguiente
            items_restantes.remove(primero_alfabeticamente)
