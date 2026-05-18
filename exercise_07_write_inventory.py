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
    resultado_final = {}
    
    with open(filename, 'r') as archivo:
        for linea in archivo:
            linea_limpia = linea.strip()
            
            # Si la línea tiene datos (no está vacía)
            if linea_limpia: 
                
                # PRIMER CORTE: Separamos el nombre del "choclo" de notas
                nombre, bloque_notas = linea_limpia.split(':')
                # nombre = 'Ana'
                # bloque_notas = '8,9,7'
                # quedaria una lista la cual es ['Ana', '8,9,7']
                # SEGUNDO CORTE: Cortamos las notas por las comas
                lista_notas_texto = bloque_notas.split(',')  #solo se lo hace a las notas, el nombre queda
                # lista_notas_texto = ['8', '9', '7']
                
                # PASAR A NÚMEROS: Como están como texto, las pasamos a float
                lista_notas_numeros = []
                for nota_txt in lista_notas_texto:
                    lista_notas_numeros.append(float(nota_txt))
                # lista_notas_numeros = [8.0, 9.0, 7.0]
                
                # LOS TRES CÁLCULOS:
                promedio = sum(lista_notas_numeros) / len(lista_notas_numeros)
                maximo = max(lista_notas_numeros)
                minimo = min(lista_notas_numeros)
                
                # GUARDAR EN EL DICCIONARIO:
                # La clave es el nombre, y el valor es la tupla (promedio, max, min)
                resultado_final[nombre] = (promedio, maximo, minimo)
                
    return resultado_final
