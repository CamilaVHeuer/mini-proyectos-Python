# Funciones para validar entradas del usuario

import re

# --- Funciones auxiliares ---
def validar_nombre(texto: str, permitir_cancelar=True):
    """
    Valida el nombre del producto ingresado por el usuario.
    - Elimina espacios iniciales/finales y capitaliza la palabra.
    - Retorna:
        'cancelado' si el usuario ingresa cancelar/volver/salir.
        'vacio' si la entrada está vacía.
        'invalido' si contiene caracteres no permitidos.
        texto limpio si es válido.
    """
    texto = texto.strip().lower()
    #valido si el usuario quiere cancelar
    if permitir_cancelar and texto in ['cancelar', 'volver', 'salir']:
        return "cancelado"
    #valido si la entrada está vacía
    if texto == "":
        return "vacio"
    #valido si la entrada contiene caracteres no permitidos
    if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", texto):
        return "invalido"
    #si todo está bien, retorno el texto limpio
    return texto

def validar_tipo(tipo_str: str):
    """
    Valida que el tipo sea 'fruta' o 'verdura'.
    """
    tipo_str = tipo_str.strip().lower()
    if tipo_str in ['cancelar', 'volver', 'salir']:
        return 'cancelado'
    if tipo_str not in ['fruta', 'verdura']:
        return 'invalido'
    return tipo_str

def validar_precio(precio_str: str):
    """
    Valida que el precio sea un número positivo.
    Retorna:
        'cancelado' si el usuario ingresa cancelar/volver/salir.
        'invalido' si no es un número o es <= 0.
        float(precio) si es válido.
    """
    precio_str = precio_str.strip().lower()
    if precio_str in ['cancelar', 'volver', 'salir']:
        return 'cancelado'
    try:
        precio = float(precio_str)
        if precio <= 0:
            return 'invalido'
        return precio
    except ValueError:
        return 'invalido'

def validar_stock(stock_str: str):
    """
    Valida que el stock sea un número entero no negativo.
    """
    stock_str = stock_str.strip().lower()
    if stock_str in ['cancelar', 'volver', 'salir']:
        return 'cancelado'
    if not stock_str.isdigit():
        return 'invalido'
    stock = int(stock_str)
    return stock

