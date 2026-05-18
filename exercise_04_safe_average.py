# Ejercicio 4 - Promedio seguro con manejo de errores


def safe_average(filename):
    """
    Lee un archivo donde hay UN número por línea y retorna el promedio de
    los números válidos (como float).

    Reglas:
    - Las líneas que no se puedan convertir a float deben ignorarse (usar
      try/except ValueError internamente).
    - Las líneas vacías también se ignoran.
    - Si el archivo no existe, propagar FileNotFoundError.
    - Si el archivo existe pero no contiene ningún número válido, lanzar
      ValueError("no valid numbers").

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        float - promedio de los números válidos.

    Raises:
        FileNotFoundError: si el archivo no existe.
        ValueError: si no hay números válidos en el archivo.

    Ejemplo:
        # archivo contiene: "10\n20\nno_es_un_numero\n30\n"
        safe_average("numeros.txt") -> 20.0
    """
    suma_total = 0
    cantidad_numeros = 0
    
    # 1. Abrimos el archivo. Si no existe, explota solo (FileNotFoundError)
    with open(filename, 'r') as archivo:
        for linea in archivo:
            linea_limpia = linea.strip()
            
            if linea_limpia: # Si la línea no está vacía
                try:
                    # 2. Intentamos convertir la línea a número decimal
                    numero = float(linea_limpia)
                    suma_total += numero
                    cantidad_numeros += 1
                except ValueError:
                    # 3. Si no era un número (ej: "hola"), Python tira ValueError. 
                    # Con 'pass' le decimos: "No hagas nada, ignoralo y pasá a la siguiente línea"
                    pass 
                    
    # 4. Palito del test: Si el archivo existía pero no se cargó ningún número válido
    if cantidad_numeros == 0:
        raise ValueError("no valid numbers")
        
    # 5. Si todo salió bien, calculamos el promedio
    return suma_total / cantidad_numeros
