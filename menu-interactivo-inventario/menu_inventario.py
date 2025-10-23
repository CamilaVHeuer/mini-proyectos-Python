#Implementación de un menú para gestionar
#una lista de frutas con funciones.
#se podrá agregar, mostrar y eliminar frutas de la lista.
#El programa presentará un menú que le permitirá al usuario elegir qué acción desea realizar.

#En primer lugar, definimos una lista vacía llamada frutas que almacenará los nombres de
# las frutas. Luego, crearemos tres funciones: una para agregar frutas, otra para consultar
# la lista de frutas, y una más para borrar una fruta específica. Finalmente,implementaremos una función para mostrar el menú y permitir que se seleccione una
# opción.

import re

productos = {}  # Diccionario para almacenar las frutas

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

# -- Funciones principales del menú --
def intentar_agregar_producto():
    nombre_producto = input('Ingrese el nombre del producto que desea agregar (o "cancelar" para volver al menú): ')
    nombre = validar_nombre(nombre_producto)
    if nombre == "cancelado":
        print("Operación cancelada. Volviendo al menú principal.\n")
        return ('cancelado', None)  #volver al menú principal
    if nombre == "vacio":
        print("No se ingresó ningún producto, por favor intente nuevamente.\n")
        return ('vacio', None)  # Salgo de la función sin agregar nada
    if nombre == "invalido":
        print("El producto debe contener solo letras y espacios, sin números ni caracteres especiales.\n")
        return ('invalido', None)  # Salgo de la función sin agregar nada
    if nombre in productos:
        print("El producto ya está en la lista.\n")
        return ('duplicado', nombre)  # Salgo de la función sin agregar nada
    
    tipo_producto = input('Ingrese el tipo de producto (fruta/verdura) (o "cancelar" para volver al menú): ')
    tipo = validar_tipo(tipo_producto)
    if tipo == 'cancelado':
        print("Operación cancelada. Volviendo al menú principal.\n")
        return ('cancelado', None)  #volver al menú principal
    if tipo == 'invalido':
        print("El tipo de producto debe ser 'fruta' o 'verdura'.\n")
        return ('invalido', None)  # Salgo de la función sin agregar nada
    
    precio_producto = input('Ingrese el precio del producto (o "cancelar" para volver al menú): ')
    precio = validar_precio(precio_producto)
    if precio == 'cancelado':
        print("Operación cancelada. Volviendo al menú principal.\n")
        return ('cancelado', None)  #volver al menú principal
    if precio == 'invalido':
        print("El precio debe ser un número positivo.\n")
        return ('invalido', None)  # Salgo de la función sin agregar nada   
    
    stock_producto = input('Ingrese el stock del producto (o "cancelar" para volver al menú): ')
    stock = validar_stock(stock_producto)
    if stock == 'cancelado':
        print("Operación cancelada. Volviendo al menú principal.\n")
        return ('cancelado', None)  #volver al menú principal
    if stock == 'invalido':
        print("El stock debe ser un número entero no negativo.\n")
        return ('invalido', None)  # Salgo de la función sin agregar nada   
    
    # Si la entrada es válida, la agrego al diccionario
    productos[nombre] = {"tipo": tipo, "precio": precio, "stock": stock}
    print(f"✅ Producto '{nombre}' agregado con éxito.")
    return ('ok', nombre)  # Indico que se agregó el producto con éxito


def mostrar_productos():
    if productos: # Verifico si el diccionario no está vacía
        print("Lista de productos:")
        for i, (nombre, detalles) in enumerate(productos.items(), start=1):
            print(f"{i}. {nombre} - Tipo: {detalles['tipo']}, Precio: {detalles['precio']}, Stock: {detalles['stock']}")
        print()  # Línea en blanco al final de la lista
    else:
        print("No hay productos en la lista.\n")

def intentar_actualizar_producto():
    nombre_producto = input('Ingrese el nombre del producto que desea actualizar (o "cancelar" para volver al menú): ')
    nombre = validar_nombre(nombre_producto)
    if nombre == "cancelado":
        print("Operación cancelada. Volviendo al menú principal.\n")
        return ('cancelado', None)  #volver al menú principal
    if nombre == "vacio":
        print("No se ingresó ningún producto, por favor intente nuevamente.\n")
        return ('vacio', None)  # Salgo de la función sin eliminar nada
    if nombre not in productos:
        print("El producto no se encuentra en la lista.\n")
        return ('no_encontrado', None)  # Salgo de la función sin eliminar nada

    print("¿Qué desea actualizar?")
    print("1. Precio")
    print("2. Stock")
    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            nuevo_precio = input("Ingrese el nuevo precio: ")
            precio = validar_precio(nuevo_precio)
            if precio == 'invalido':
                print("El precio debe ser un número positivo.\n")
                return ('invalido', None)  # Salgo de la función sin actualizar nada
            
            productos[nombre]["precio"] = precio
            print(f"✅ Precio del producto '{nombre}' actualizado a {precio}.")
            return ('ok', nombre)  # Indico que se actualizó el producto con éxito
        
        case "2":
            nuevo_stock = input("Ingrese el nuevo stock: ")
            stock = validar_stock(nuevo_stock)
            if stock == 'invalido':
                print("El stock debe ser un número entero no negativo.\n")
                return ('invalido', None)  # Salgo de la función sin actualizar nada
            productos[nombre]["stock"] = stock
            print(f"✅ Stock del producto '{nombre}' actualizado a {stock}.")
            return ('ok', nombre)  # Indico que se actualizó el producto con éxito
        
        case _:
            print("Opción inválida. No se realizó ninguna actualización.")
            return ('invalido', None)  # Salgo de la función sin actualizar nada

def intentar_eliminar_producto():
    if not productos:
        print("No hay productos en la lista.\n")
        return ('no_encontrado', None) #volver al menú principal para evitar loop infinito
    nombre_producto = input('Ingrese el nombre del producto que desea eliminar (o "cancelar" para volver al menú): ')
    nombre = validar_nombre(nombre_producto)
    if nombre == "cancelado":
            print("Operación cancelada. Volviendo al menú principal.\n")
            return ('cancelado', None)  #volver al menú principal
    if nombre == "vacio":
            print("No se ingresó ningún producto, por favor intente nuevamente.\n")
            return ('vacio', None)  # Salgo de la función sin eliminar nada
    if nombre not in productos:
            print("El producto no se encuentra en la lista.\n")
            return ('no_encontrado', None)  # Salgo de la función sin eliminar nada

    confirmacion = input('Está seguro que desea eliminar el producto? (s/n): ').strip().lower()
    if confirmacion == 's':
        del productos[nombre]
        print(f"Producto {nombre} eliminado con éxito.\n")
        return ('ok', nombre)  # Indico que se eliminó el producto con éxito
    else:
        print("Operación cancelada.\n")
        return ('cancelado', None)  # Operación cancelada, volver al menú principal

def mostrar_menu():
    while True:
        print("\n--- Menú ---")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        print("---------------")

        opcion = input("Seleccione una opción del 1 al 5: ")
        #validar la opción ingresada
        if not opcion.isdigit() or not 1 <= int(opcion) <= 5:
            print("Opción inválida. Por favor, ingrese un número entre 1 y 5.\n")
            continue  # Volver al inicio del bucle si la opción es inválida

        match opcion:
            case "1":
                while True:
                    estado, _ = intentar_agregar_producto()
                    if estado in ["ok", "cancelado"]:
                        break
                
            case "2":
                mostrar_productos()
            case "3":
                while True:
                    estado, _ = intentar_actualizar_producto()
                    if estado in ["ok", "cancelado", "no_encontrado"]:
                        break
            case "4":
                while True:
                    estado, _ = intentar_eliminar_producto()
                    if estado in ["ok", "cancelado", "no_encontrado"]:
                        break
            case "5":
                print("Saliendo del programa...\n")
                break
