# Ejercicio 10 - Parser de archivos de log


def parse_log(filename):
    """
    Lee un archivo de log donde cada línea tiene el formato:

        NIVEL: mensaje

    y retorna un diccionario donde la clave es el nivel y el valor es una
    lista con todos los mensajes de ese nivel, en el orden en que aparecen.

    Reglas:
    - Los niveles no son fijos: cualquier string antes del primer ':'
      cuenta como nivel. El mensaje es todo lo que viene después del
      primer ':'.
    - Aplicar strip al nivel y al mensaje para eliminar espacios sobrantes.
    - Las líneas vacías (o con solo espacios) se ignoran: NO son inválidas.
    - Si alguna línea no vacía NO tiene ':', lanzar
      ValueError("invalid log line").
    - Si el archivo no existe, propagar FileNotFoundError.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        dict[str, list[str]] - mensajes agrupados por nivel.

    Raises:
        FileNotFoundError: si el archivo no existe.
        ValueError: si alguna línea no vacía no tiene ':'.

    Ejemplo:
        # archivo contiene:
        # INFO: servidor iniciado
        # ERROR: no se puede conectar
        # INFO: reintentando
        # WARN: lento
        parse_log("server.log") -> {
            "INFO": ["servidor iniciado", "reintentando"],
            "ERROR": ["no se puede conectar"],
            "WARN": ["lento"],
        }
    """
    resultado_log = {}
    
    # 1. Abrimos el archivo. Si no existe, explota solo (FileNotFoundError)
    with open(filename, 'r') as archivo:
        for linea in archivo:
            linea_limpia = linea.strip()
            
            # REGLA 1: Las líneas vacías se ignoran por completo
            if linea_limpia: 
                
                # REGLA 2: Si la línea NO tiene los dos puntos, es inválida
                if ":" not in linea_limpia:
                    raise ValueError("invalid log line")
                
                # PRIMER CORTE: Separamos el nivel del mensaje
                # Usamos split(':', 1) para que corte SOLO en el primer ':' que encuentre
                partes = linea_limpia.split(':', 1)
                
                # Limpiamos los espacios que puedan tener el nivel o el mensaje
                nivel = partes[0].strip()   # Ej: "INFO"
                mensaje = partes[1].strip() # Ej: "servidor iniciado"
                
                # GUARDAR EN DICCIONARIO DE LISTAS:
                if nivel in resultado_log:
                    resultado_log[nivel].append(mensaje) # Si ya existía el nivel, agregamos el mensaje a su lista
                else:
                    resultado_log[nivel] = [mensaje] # Si es un nivel nuevo, creamos la lista con su primer mensaje
                    
    return resultado_log
