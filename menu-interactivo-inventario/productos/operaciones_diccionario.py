# Funciones para agregar, mostrar, actualizar y eliminar productos del inventario usando diccionario
from productos.validaciones import validar_nombre, validar_tipo, validar_precio, validar_stock

productos = {}  # Diccionario para almacenar los productos

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
    print(f"✅ Producto '{nombre}' agregado exitosamente.")
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
