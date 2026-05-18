# Ejercicio 6 - Estadísticas de notas por estudiante


def grades_stats(filename):
    """
    Lee un archivo donde cada línea tiene el formato:

        estudiante:nota1,nota2,nota3,...

    y retorna un diccionario donde la clave es el nombre del estudiante y
    el valor es una TUPLA (promedio, maximo, minimo) con los tres valores
    como float.

    Reglas:
    - El promedio se calcula con todas las notas de la línea.
    - Las líneas vacías se ignoran.
    - Se garantiza que todas las notas son números válidos.
    - Si el archivo no existe, propagar FileNotFoundError.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        dict[str, tuple[float, float, float]] - estadísticas por estudiante.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene: "Ana:8,9,7\nBeto:5,5,10\nCami:10\n"
        grades_stats("notas.txt") -> {
            "Ana": (8.0, 9.0, 7.0),
            "Beto": (6.666666666666667, 10.0, 5.0),
            "Cami": (10.0, 10.0, 10.0),
        }
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
