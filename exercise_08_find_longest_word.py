# Ejercicio 8 - Palabra más larga de un archivo


def find_longest_word(filename):
    """
    Lee el archivo, lo divide en palabras (separadas por cualquier tipo
    de whitespace) y retorna la palabra más larga.

    Reglas:
    - Si hay varias palabras con la misma longitud máxima, retornar la
      PRIMERA en aparecer.
    - Si el archivo no existe, propagar FileNotFoundError.
    - Si el archivo no tiene ninguna palabra (está vacío o solo tiene
      espacios/saltos de línea), lanzar ValueError("file has no words").

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        str - la palabra más larga del archivo.

    Raises:
        FileNotFoundError: si el archivo no existe.
        ValueError: si el archivo no tiene palabras.

    Ejemplo:
        # archivo contiene: "el gato corre rapido\npor el jardin\n"
        find_longest_word("texto.txt") -> "rapido"
    """
palabra_ganadora = ""
    max_letras = -1  # Empezamos con un piso bien bajo
    
    # 1. Abrimos y leemos todo el archivo
    with open(filename, 'r') as archivo:
        contenido = archivo.read()
        
        # 2. Pasamos la tijera para separar por espacios y saltos de línea
        lista_palabras = contenido.split() 
        # Si el archivo decía "el gato corre", lista_palabras es ['el', 'gato', 'corre']
        
    # 3. El palito del test: Si el archivo estaba vacío, la lista queda []
    if len(lista_palabras) == 0:
        raise ValueError("file has no words") # Plantamos bandera de error
        
    # 4. El bucle para buscar la más larga (Como buscar el mayor puntaje)
    for palabra in lista_palabras:
        
        # len(palabra) nos dice cuántas letras tiene la palabra actual
        if len(palabra) > max_letras:
            max_letras = len(palabra)  # Guardamos el nuevo récord de letras
            palabra_ganadora = palabra # Guardamos la palabra que rompió el récord
            
    return palabra_ganadora
