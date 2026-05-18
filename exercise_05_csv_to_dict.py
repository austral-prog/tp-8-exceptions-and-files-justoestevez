# Ejercicio 5 - CSV a lista de diccionarios


def csv_to_dict(filename):
    """
    Lee un archivo CSV con header "name,age,city" y retorna una lista de
    diccionarios, uno por fila.

    Reglas:
    - La primera línea es siempre el header.
    - Las claves del diccionario se toman del header.
    - El campo "age" se convierte a int. "name" y "city" quedan como str.
    - Se deben hacer strip a los valores para eliminar espacios sobrantes.
    - Si el archivo está vacío o solo tiene header, retornar [].
    - Si el archivo no existe, propagar FileNotFoundError.
    - No se permite usar el módulo csv.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        list[dict] - lista de diccionarios por fila del CSV.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene:
        # name,age,city
        # Alice,30,Buenos Aires
        # Bob,25,Rosario
        csv_to_dict("people.csv") -> [
            {"name": "Alice", "age": 30, "city": "Buenos Aires"},
            {"name": "Bob", "age": 25, "city": "Rosario"},
        ]
    """
    resultado = []
    
    with open(filename, 'r') as archivo:
        # 1. Leemos todas las líneas del archivo juntas
        lineas = archivo.readlines()
        
    # 2. Si el archivo está vacío o solo tiene la primera línea (el encabezado/header), devolvemos []
    if len(lineas) <= 1:
        return []
        
    # 3. La primera línea es SIEMPRE el encabezado ("name,age,city")
    # Le sacamos los espacios y la cortamos por las comas
    encabezado = lineas[0].strip().split(',') # Esto da: ['name', 'age', 'city']
    
    # 4. Recorremos las demás líneas (desde la posición 1 en adelante)
    for linea in lineas[1:]:
        linea_limpia = linea.strip()
        
        if linea_limpia: # Si la línea tiene datos
            # Cortamos los datos de la persona por la comas
            datos = linea_limpia.split(',') # Ej: ['Alice', '30', 'Buenos Aires']
            
            # 5. Armamos el diccionario para esta persona usando las claves del encabezado
            persona_dict = {
                'name': datos[0],
                'age': int(datos[1]), # Obligatorio pasarlo a número entero
                'city': datos[2]
            }
            
            # Guardamos el diccionario de esta persona en nuestra lista final
            resultado.append(persona_dict)
            
    return resultado
